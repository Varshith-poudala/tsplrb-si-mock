import { NextResponse } from 'next/server';
import crypto from 'crypto';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Payment from '@/models/Payment';

export async function POST(req) {
  try {
    const rawBody = await req.json();
    const xVerifyHeader = req.headers.get('x-verify');
    const saltKey = process.env.PHONEPE_SALT_KEY;
    const saltIndex = process.env.PHONEPE_SALT_INDEX || '1';

    if (!rawBody?.response) {
      return NextResponse.json({ error: 'Missing response payload' }, { status: 400 });
    }

    // 1. Verify Cryptographic Signature from PhonePe Server
    if (saltKey && xVerifyHeader) {
      const calculatedHash = crypto
        .createHash('sha256')
        .update(rawBody.response + saltKey)
        .digest('hex');
      const expectedVerify = `${calculatedHash}###${saltIndex}`;

      if (xVerifyHeader !== expectedVerify) {
        console.error('❌ PhonePe Signature Mismatch! Rejecting fraudulent callback.');
        return NextResponse.json({ error: 'Invalid signature' }, { status: 400 });
      }
    }

    // 2. Decode Base64 Payload from PhonePe
    const decodedBuffer = Buffer.from(rawBody.response, 'base64');
    const payload = JSON.parse(decodedBuffer.toString('utf-8'));

    console.log('🔔 PhonePe Webhook Event:', payload.code, payload.data?.merchantTransactionId);

    const transactionId = payload.data?.merchantTransactionId;
    const isSuccess = payload.code === 'PAYMENT_SUCCESS' && payload.data?.responseCode === 'SUCCESS';

    const conn = await connectToDatabase();
    if (conn && transactionId) {
      const payment = await Payment.findOne({ transactionId });

      if (payment) {
        payment.status = isSuccess ? 'completed' : 'failed';
        payment.orderId = payload.data?.transactionId || '';
        await payment.save();

        if (isSuccess && payment.userEmail) {
          // Unlock candidate in MongoDB
          await User.findOneAndUpdate(
            { email: payment.userEmail.toLowerCase() },
            {
              isPaid: true,
              accessGrantedBy: 'payment',
              accessGrantedAt: new Date(),
              notes: `PhonePe PG TransID: ${payload.data?.transactionId}`,
            }
          );
          console.log(`✅ Candidate ${payment.userEmail} unlocked automatically via PhonePe PG!`);
        }
      }
    }

    return NextResponse.json({ success: true, message: 'Webhook processed' });
  } catch (err) {
    console.error('PhonePe callback processing error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
