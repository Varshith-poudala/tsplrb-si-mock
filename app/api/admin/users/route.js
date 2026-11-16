import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Attempt from '@/models/Attempt';
import Payment from '@/models/Payment';

// Helper to check if current user is admin
async function checkAdmin(session) {
  if (!session?.user?.email) return false;
  const adminEmails = (process.env.ADMIN_EMAILS || 'varshithpoudala@gmail.com')
    .toLowerCase()
    .split(',')
    .map(e => e.trim());
  return adminEmails.includes(session.user.email.toLowerCase()) || session.user.role === 'admin';
}

export async function GET(req) {
  try {
    const session = await getServerSession(authOptions);
    const isAdmin = await checkAdmin(session);

    if (!isAdmin) {
      return NextResponse.json({ error: 'Unauthorized: Admin access required' }, { status: 403 });
    }

    const conn = await connectToDatabase();
    if (!conn) {
      return NextResponse.json({
        users: [
          {
            _id: 'admin_local',
            name: 'Varshith (Super Admin)',
            email: 'varshithpoudala@gmail.com',
            role: 'admin',
            isPaid: true,
            accessGrantedBy: 'admin',
            attemptsCount: 0,
            notes: 'Master Administrator Account',
          }
        ],
        stats: { totalUsers: 1, paidUsers: 1, adminGrants: 1, freeUsers: 0 }
      });
    }

    const users = await User.find({}).sort({ createdAt: -1 }).lean();

    // Attach attempt count for each user
    const usersWithStats = await Promise.all(
      users.map(async (u) => {
        const attemptsCount = await Attempt.countDocuments({ userEmail: u.email });
        return {
          ...u,
          _id: u._id.toString(),
          attemptsCount,
        };
      })
    );

    const stats = {
      totalUsers: users.length,
      paidUsers: users.filter(u => u.isPaid).length,
      adminGrants: users.filter(u => u.accessGrantedBy === 'admin').length,
      freeUsers: users.filter(u => !u.isPaid).length,
    };

    return NextResponse.json({ users: usersWithStats, stats });
  } catch (err) {
    console.error('Admin users GET error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

export async function POST(req) {
  try {
    const session = await getServerSession(authOptions);
    const isAdmin = await checkAdmin(session);

    if (!isAdmin) {
      return NextResponse.json({ error: 'Unauthorized: Admin access required' }, { status: 403 });
    }

    const { email, isPaid, notes } = await req.json();

    if (!email) {
      return NextResponse.json({ error: 'Email is required' }, { status: 400 });
    }

    await connectToDatabase();
    const cleanEmail = email.toLowerCase().trim();

    let user = await User.findOne({ email: cleanEmail });

    if (!user) {
      // Pre-authorize user before they even log in for the first time!
      user = await User.create({
        email: cleanEmail,
        name: cleanEmail.split('@')[0],
        role: 'user',
        isPaid: Boolean(isPaid),
        accessGrantedBy: isPaid ? 'admin' : null,
        accessGrantedAt: isPaid ? new Date() : null,
        notes: notes || 'Pre-authorized by Admin',
      });
    } else {
      user.isPaid = Boolean(isPaid);
      user.accessGrantedBy = isPaid ? 'admin' : null;
      user.accessGrantedAt = isPaid ? new Date() : null;
      if (notes) user.notes = notes;
      await user.save();
    }

    // Log this action in Payment history for record keeping
    if (isPaid) {
      await Payment.create({
        userId: user._id,
        userEmail: cleanEmail,
        amount: 0,
        currency: 'INR',
        gateway: 'admin_manual',
        transactionId: `ADM_GRANT_${Date.now()}_${Math.random().toString(36).substring(7).toUpperCase()}`,
        status: 'completed',
        adminGrantedBy: session.user.email,
      });
    }

    return NextResponse.json({
      success: true,
      message: isPaid
        ? `✅ Successfully granted Full Access to ${cleanEmail} without any payment!`
        : `⚠️ Revoked full access for ${cleanEmail}`,
      user: {
        email: user.email,
        isPaid: user.isPaid,
        accessGrantedBy: user.accessGrantedBy,
      },
    });
  } catch (err) {
    console.error('Admin grant POST error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
