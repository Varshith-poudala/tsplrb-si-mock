import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import crypto from 'crypto';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Payment from '@/models/Payment';

export const dynamic = 'force-dynamic';

export async function POST(req) {
  try {
    const session = await getServerSession(authOptions);
    const body = await req.json();
    const { razorpay_order_id, razorpay_payment_id, razorpay_signature } = body;

    if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature) {
      return NextResponse.json({ error: 'Missing payment signature details' }, { status: 400 });
    }

    // Explicitly use the live secret, overriding any global test keys from the OS
    const keySecret = 'Jz50CYzJ9dxOdG61gbTC8q2P';
    if (!keySecret) {
      return NextResponse.json({ error: 'Razorpay secret key not configured' }, { status: 500 });
    }

    // 1. Verify Cryptographic Signature
    const expectedSignature = crypto
      .createHmac('sha256', keySecret)
      .update(`${razorpay_order_id}|${razorpay_payment_id}`)
      .digest('hex');

    if (expectedSignature !== razorpay_signature) {
      console.error('❌ Razorpay Signature Mismatch! Rejecting fraudulent request.');
      return NextResponse.json({ error: 'Invalid payment signature' }, { status: 400 });
    }

    // 2. Signature is 100% Genuine! Unlock candidate in MongoDB
    const userEmail = (session?.user?.email || body.userEmail || '').toLowerCase();
    const conn = await connectToDatabase();

    if (conn && userEmail) {
      let dbUser = await User.findOne({ email: userEmail });
      if (!dbUser) {
        dbUser = await User.create({
          email: userEmail,
          name: session?.user?.name || userEmail.split('@')[0],
          role: 'user',
          isPaid: true,
          accessGrantedBy: 'payment',
          accessGrantedAt: new Date(),
          notes: `Razorpay Payment ID: ${razorpay_payment_id}`,
        });
      } else {
        dbUser.isPaid = true;
        dbUser.accessGrantedBy = 'payment';
        dbUser.accessGrantedAt = new Date();
        dbUser.notes = `Razorpay Payment ID: ${razorpay_payment_id}`;
        await dbUser.save();
      }

      await Payment.findOneAndUpdate(
        { orderId: razorpay_order_id },
        {
          userId: dbUser._id,
          userEmail,
          amount: Number(process.env.TEST_SERIES_PRICE || 99),
          currency: 'INR',
          gateway: 'razorpay',
          transactionId: razorpay_payment_id,
          status: 'completed',
        },
        { upsert: true, new: true }
      );

      console.log(`✅ Candidate ${userEmail} successfully unlocked via Razorpay (${razorpay_payment_id})!`);
    }

    return NextResponse.json({
      success: true,
      message: '🎉 Payment Verified! All full-length 200-question exams are now unlocked.',
      paymentId: razorpay_payment_id,
      isPaid: true,
    });
  } catch (err) {
    console.error('Razorpay verification error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
