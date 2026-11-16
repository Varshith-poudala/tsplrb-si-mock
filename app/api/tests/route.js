import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import Test from '@/models/Test';
import User from '@/models/User';

export const dynamic = 'force-dynamic';

export async function GET(req) {
  try {
    const session = await getServerSession(authOptions);
    let isUserPaid = false;
    let isAdmin = false;

    if (session?.user?.email) {
      const email = session.user.email.toLowerCase();
      const adminEmails = (process.env.ADMIN_EMAILS || 'varshithpoudala@gmail.com')
        .toLowerCase()
        .split(',')
        .map(e => e.trim());

      isAdmin = adminEmails.includes(email);

      const conn = await connectToDatabase();
      if (conn) {
        const dbUser = await User.findOne({ email });
        if (dbUser?.isPaid || isAdmin) {
          isUserPaid = true;
        }
      } else if (isAdmin) {
        isUserPaid = true;
      }
    }

    // Default predefined test catalog
    const testCatalog = [
      {
        testId: 'demo-test-50',
        title: 'TSPLRB SI Free Demo Mock Test (50 Questions)',
        title_te: 'తెలంగాణ ఎస్సై ఉచిత డెమో మాక్ టెస్ట్ (50 ప్రశ్నలు)',
        exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
        totalQuestions: 50,
        totalMarks: 50,
        durationMinutes: 45,
        marksPerQuestion: 1.0,
        negativeMarking: 0.20,
        isFreeDemo: true,
        isUnlocked: true,
        description: 'Comprehensive 50-Question Free Demo featuring Arithmetic, Reasoning, and Current Affairs.',
      },
      {
        testId: 'tsplrb-si-mock-full-200',
        title: 'TSPLRB SI Full-Length Mock Test 1 (200 Questions)',
        title_te: 'తెలంగాణ ఎస్సై పూర్తి స్థాయి మాక్ టెస్ట్ 1 (200 ప్రశ్నలు)',
        exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
        totalQuestions: 200,
        totalMarks: 200,
        durationMinutes: 180,
        marksPerQuestion: 1.0,
        negativeMarking: 0.20,
        isFreeDemo: false,
        isUnlocked: isUserPaid,
        description: 'Official 200-Question Exam Pattern: 50 Arithmetic + 50 Reasoning + 100 General Studies & Telangana Movement.',
      },
      {
        testId: 'tsplrb-si-mock-full-200-2',
        title: 'TSPLRB SI Full-Length Mock Test 2 (200 Questions)',
        title_te: 'తెలంగాణ ఎస్సై పూర్తి స్థాయి మాక్ టెస్ట్ 2 (200 ప్రశ్నలు)',
        exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
        difficulty: 'Medium',
        totalQuestions: 200,
        totalMarks: 200,
        durationMinutes: 180,
        marksPerQuestion: 1.0,
        negativeMarking: 0.20,
        isFreeDemo: false,
        isUnlocked: isUserPaid,
        description: 'Advanced Practice Paper with In-depth Focus on Telangana History and High-Difficulty Reasoning.',
      },
      {
        testId: 'tsplrb-si-mock-full-200-3',
        title: 'TSPLRB SI Mock Test 3 (Easy • Foundational PWT)',
        title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 3 (సులభం • ప్రాథమిక స్థాయి PWT)',
        exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
        difficulty: 'Easy',
        totalQuestions: 200,
        totalMarks: 200,
        durationMinutes: 180,
        marksPerQuestion: 1.0,
        negativeMarking: 0.20,
        isFreeDemo: false,
        isUnlocked: isUserPaid,
        description: 'Foundational 200Q paper focusing on core formulas, direct arithmetic, standard reasoning, and essential General Studies.',
      },
      {
        testId: 'tsplrb-si-mock-full-200-4',
        title: 'TSPLRB SI Mock Test 4 (Medium • Official Standard PWT)',
        title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 4 (మధ్యస్థం • అధికారిక ప్రామాణిక PWT)',
        exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
        difficulty: 'Medium',
        totalQuestions: 200,
        totalMarks: 200,
        durationMinutes: 180,
        marksPerQuestion: 1.0,
        negativeMarking: 0.20,
        isFreeDemo: false,
        isUnlocked: isUserPaid,
        description: 'Exact calibration of the official TSPLRB SI 2022 Preliminary Exam. Standard multi-step word problems and official Telangana Movement history.',
      },
      {
        testId: 'tsplrb-si-mock-full-200-5',
        title: 'TSPLRB SI Mock Test 5 (Tough • Advanced High-Yield PWT)',
        title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 5 (క్లిష్టం • ఉన్నత స్థాయి స్పెషల్ PWT)',
        exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
        difficulty: 'Tough',
        totalQuestions: 200,
        totalMarks: 200,
        durationMinutes: 180,
        marksPerQuestion: 1.0,
        negativeMarking: 0.20,
        isFreeDemo: false,
        isUnlocked: isUserPaid,
        description: 'High-difficulty 200Q simulation modeling recent TSPSC and TSPLRB trends. Advanced statement-based questions, intricate puzzles, and in-depth governance.',
      }
    ];

    return NextResponse.json({
      tests: testCatalog,
      userAccess: {
        isLoggedIn: Boolean(session?.user),
        email: session?.user?.email || null,
        isPaid: isUserPaid,
        isAdmin,
      }
    });
  } catch (err) {
    console.error('Tests GET error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
