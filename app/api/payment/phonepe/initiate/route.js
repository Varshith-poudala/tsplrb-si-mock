import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Payment from '@/models/Payment';
import crypto from 'crypto';

export async function POST(req) {
  try {
    const session = await getServerSession(authOptions);
    if (!session?.user?.email) {
      return NextResponse.json({ error: 'Please sign in to proceed with payment' }, { status: 401 });
    }

    const amount = Number(process.env.TEST_SERIES_PRICE || 99);
    const userEmail = session.user.email.toLowerCase();
    const transactionId = `TXN_${Date.now()}_${Math.random().toString(36).substring(7).toUpperCase()}`;

    const conn = await connectToDatabase();
    let dbUser = null;
    if (conn) {
      dbUser = await User.findOne({ email: userEmail });
      if (!dbUser) {
        dbUser = await User.create({
          email: userEmail,
          name: session.user.name || 'Candidate',
          role: 'user',
          isPaid: false,
        });
      }
    }

    const userIdStr = dbUser?._id ? dbUser._id.toString() : userEmail;

    // Check PhonePe Business PG Merchant credentials
    const merchantId = process.env.PHONEPE_MERCHANT_ID;
    const saltKey = process.env.PHONEPE_SALT_KEY;
    const saltIndex = process.env.PHONEPE_SALT_INDEX || '1';
    const envMode = process.env.PHONEPE_ENV || 'PRODUCTION'; // 'UAT' or 'PRODUCTION'

    if (merchantId && saltKey) {
      const baseUrl = process.env.NEXTAUTH_URL || 'http://localhost:3000';
      const payload = {
        merchantId,
        merchantTransactionId: transactionId,
        merchantUserId: userIdStr,
        amount: amount * 100, // paise (99 * 100 = 9900)
        redirectUrl: `${baseUrl}/payment/status?id=${transactionId}`,
        redirectMode: 'POST',
        callbackUrl: `${baseUrl}/api/payment/phonepe/callback`,
        paymentInstrument: {
          type: 'PAY_PAGE',
        },
      };

      const base64Payload = Buffer.from(JSON.stringify(payload)).toString('base64');
      const stringToHash = base64Payload + '/pg/v1/pay' + saltKey;
      const sha256 = crypto.createHash('sha256').update(stringToHash).digest('hex');
      const xVerify = `${sha256}###${saltIndex}`;

      const phonepeApiEndpoint = envMode === 'UAT'
        ? 'https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/pay'
        : 'https://api.phonepe.com/apis/hermes/pg/v1/pay';

      try {
        const pgResponse = await fetch(phonepeApiEndpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-VERIFY': xVerify,
          },
          body: JSON.stringify({ request: base64Payload }),
        });

        const pgData = await pgResponse.json();

        if (pgData.success && pgData.data?.instrumentResponse?.redirectInfo?.url) {
          // Log payment intent in MongoDB
          if (conn) {
            await Payment.create({
              userId: dbUser?._id,
              userEmail,
              amount,
              currency: 'INR',
              gateway: 'phonepe',
              transactionId,
              orderId: pgData.data.merchantTransactionId,
              status: 'pending',
            });
          }

          return NextResponse.json({
            gateway: 'phonepe_pg',
            redirectUrl: pgData.data.instrumentResponse.redirectInfo.url,
            transactionId,
          });
        } else {
          console.error('PhonePe PG Error Response:', pgData);
        }
      } catch (pgErr) {
        console.error('PhonePe PG network call failed:', pgErr.message);
      }
    }

    // Direct UPI Intent / Dynamic QR Code fallback (e.g. if PG keys not added yet)
    const upiVpa = process.env.MERCHANT_UPI_VPA || 'varshithpoudala@ybl';
    const upiName = encodeURIComponent(process.env.MERCHANT_UPI_NAME || 'TSPLRB Mock Series');
    const note = encodeURIComponent(`TSPLRB SI Mock Test Series - ${userEmail}`);
    const upiIntentUrl = `upi://pay?pa=${upiVpa}&pn=${upiName}&am=${amount}&cu=INR&tn=${note}&tr=${transactionId}`;

    if (conn) {
      await Payment.create({
        userId: dbUser?._id,
        userEmail,
        amount,
        currency: 'INR',
        gateway: 'phonepe',
        transactionId,
        status: 'pending',
      });
    }

    return NextResponse.json({
      gateway: 'upi_intent',
      transactionId,
      amount,
      upiVpa,
      upiIntentUrl,
      qrUrl: `https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=${encodeURIComponent(upiIntentUrl)}`,
    });
  } catch (err) {
    console.error('Payment initiation error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
