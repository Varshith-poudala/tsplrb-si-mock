import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Payment from '@/models/Payment';

export const dynamic = 'force-dynamic';

export async function POST(req) {
  try {
    const session = await getServerSession(authOptions);
    let body = {};
    try {
      body = await req.json();
    } catch (e) {}

    const userEmail = (session?.user?.email || body?.email || 'candidate@tsplrb.com').toLowerCase();

    // Explicitly use the live credentials, overriding any global test keys from the OS
    const keyId = 'rzp_live_TzeZXZ5JhJqX4z';
    const keySecret = 'Jz50CYzJ9dxOdG61gbTC8q2P';

    if (!keyId || !keySecret) {
      return NextResponse.json({ error: 'Razorpay keys not configured' }, { status: 500 });
    }

    const amount = Number(process.env.TEST_SERIES_PRICE || 99);
    const amountInPaise = amount * 100; // 9900

    // Call Razorpay Orders API
    const authHeader = 'Basic ' + Buffer.from(`${keyId}:${keySecret}`).toString('base64');

    const orderPayload = {
      amount: amountInPaise,
      currency: 'INR',
      receipt: `rcpt_${Date.now()}_${Math.random().toString(36).substring(7)}`,
      notes: {
        userEmail,
        examName: 'TSPLRB SI Mock Test Series',
      },
    };

    const rzpRes = await fetch('https://api.razorpay.com/v1/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: authHeader,
      },
      body: JSON.stringify(orderPayload),
    });

    const orderData = await rzpRes.json();

    if (!rzpRes.ok) {
      console.error('Razorpay Order API Error:', orderData);
      return NextResponse.json(
        { error: orderData.error?.description || 'Failed to create Razorpay order' },
        { status: 500 }
      );
    }

    // Record pending transaction in MongoDB
    try {
      const conn = await connectToDatabase();
      if (conn) {
        let dbUser = await User.findOne({ email: userEmail });
        if (!dbUser) {
          dbUser = await User.create({
            email: userEmail,
            name: session?.user?.name || 'Candidate',
            role: 'user',
            isPaid: false,
          });
        }

        await Payment.create({
          userId: dbUser._id,
          userEmail,
          amount,
          currency: 'INR',
          gateway: 'razorpay',
          transactionId: orderData.id,
          orderId: orderData.id,
          status: 'pending',
        });
      }
    } catch (dbErr) {
      console.warn('Could not record pending payment:', dbErr.message);
    }

    return NextResponse.json({
      success: true,
      orderId: orderData.id,
      amount: orderData.amount,
      currency: orderData.currency,
      keyId,
      user: {
        name: session?.user?.name || '',
        email: userEmail,
      },
    });
  } catch (err) {
    console.error('Create order error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
