import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Payment from '@/models/Payment';

export async function POST(req) {
  try {
    const session = await getServerSession(authOptions);
    if (!session?.user?.email) {
      return NextResponse.json({ error: 'Please sign in to verify payment' }, { status: 401 });
    }

    const { transactionId, utrNumber } = await req.json();

    if (!utrNumber || utrNumber.trim().length < 8) {
      return NextResponse.json(
        { error: 'Please enter a valid 12-digit UPI reference (UTR) number.' },
        { status: 400 }
      );
    }

    const cleanUtr = utrNumber.trim();
    const userEmail = session.user.email.toLowerCase();
    const conn = await connectToDatabase();

    if (conn) {
      const dbUser = await User.findOne({ email: userEmail });
      if (dbUser) {
        dbUser.notes = `Submitted UTR: ${cleanUtr} (Pending Admin Approval)`;
        await dbUser.save();
      }

      await Payment.findOneAndUpdate(
        { userEmail, transactionId: transactionId || { $exists: true } },
        {
          utrNumber: cleanUtr,
          status: 'pending',
          amount: Number(process.env.TEST_SERIES_PRICE || 99),
        },
        { upsert: true, new: true }
      );
    }

    return NextResponse.json({
      success: true,
      pending: true,
      message: '✅ UTR received! Your payment reference has been submitted. Access will be unlocked shortly once verified.',
    });
  } catch (err) {
    console.error('UTR verify error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
