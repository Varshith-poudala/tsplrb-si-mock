import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Question from '@/models/Question';
import fs from 'fs';
import path from 'path';

export async function GET(req, { params }) {
  try {
    const { id } = params;
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

      try {
        const conn = await connectToDatabase();
        if (conn) {
          const dbUser = await User.findOne({ email });
          if (dbUser?.isPaid || isAdmin) {
            isUserPaid = true;
          }
        } else if (isAdmin) {
          isUserPaid = true;
        }
      } catch (e) {
        if (isAdmin) isUserPaid = true;
      }
    }

    const isDemo = id === 'demo-test-50';

    // Gate full exams behind payment or admin access
    if (!isDemo && !isUserPaid && !isAdmin) {
      return NextResponse.json(
        {
          error: 'Payment Required',
          message: 'This 200-question full exam requires full access. Unlock all exams for ₹99.',
          requiresPayment: true,
        },
        { status: 402 }
      );
    }

    let questionsData = [];

    // Try fetching from MongoDB first
    try {
      const conn = await connectToDatabase();
      if (conn) {
        const dbQuestions = await Question.find({ testId: id }).sort({ qNumber: 1 }).lean();
        if (dbQuestions && dbQuestions.length > 0) {
          questionsData = dbQuestions;
        }
      }
    } catch (e) {
      console.warn('DB lookup failed, falling back to local dataset');
    }

    // Fallback to local verified JSON dataset if DB is not seeded yet
    if (!questionsData || questionsData.length === 0) {
      let fileName = 'mock_test_full_200.json';
      if (id === 'tsplrb-si-mock-full-200-3') fileName = 'mock_test_full_200_3.json';
      else if (id === 'tsplrb-si-mock-full-200-4') fileName = 'mock_test_full_200_4.json';
      else if (id === 'tsplrb-si-mock-full-200-5') fileName = 'mock_test_full_200_5.json';

      const localFilePath = path.join(process.cwd(), 'public/data', fileName);
      if (fs.existsSync(localFilePath)) {
        const fileContent = fs.readFileSync(localFilePath, 'utf-8');
        const parsed = JSON.parse(fileContent);
        questionsData = parsed.questions || [];
      }
    }

    // If Demo test requested, take the first 50 representative questions
    if (isDemo && questionsData.length > 50) {
      // Pick 20 Arithmetic + 15 Reasoning + 15 GS
      const arith = questionsData.slice(0, 20);
      const reasoning = questionsData.slice(50, 65);
      const gs = questionsData.slice(100, 115);
      questionsData = [...arith, ...reasoning, ...gs].map((q, idx) => ({
        ...q,
        id: idx + 1,
        qNumber: idx + 1,
      }));
    }

    // SANITIZATION STEP: Strip answers and explanations completely!
    // The browser inspect tab will NEVER see the answers!
    const sanitizedQuestions = questionsData.map((q) => {
      return {
        id: q.id || q.qNumber,
        qNumber: q.qNumber || q.id,
        section: q.section,
        topic: q.topic || '',
        question_en: q.question_en,
        question_te: q.question_te,
        options_en: q.options_en,
        options_te: q.options_te,
      };
    });

    let testTitle = isDemo ? 'TSPLRB SI Free Demo Mock Test' : 'TSPLRB SI Full-Length Mock Test';
    if (id === 'tsplrb-si-mock-full-200-3') testTitle = 'TSPLRB SI Mock Test 3 (Easy • Foundational)';
    else if (id === 'tsplrb-si-mock-full-200-4') testTitle = 'TSPLRB SI Mock Test 4 (Medium • Official Standard)';
    else if (id === 'tsplrb-si-mock-full-200-5') testTitle = 'TSPLRB SI Mock Test 5 (Tough • Advanced High-Yield)';
    else if (id === 'tsplrb-si-mock-full-200-2') testTitle = 'TSPLRB SI Mock Test 2 (High Yield Practice)';
    else if (id === 'tsplrb-si-mock-full-200') testTitle = 'TSPLRB SI Mock Test 1 (Full 200 Qs)';

    const testMeta = {
      testId: id,
      title: testTitle,
      totalQuestions: sanitizedQuestions.length,
      durationMinutes: isDemo ? 45 : 180,
      negativeMarking: 0.20,
      marksPerQuestion: 1.0,
      questions: sanitizedQuestions,
    };

    return NextResponse.json(testMeta);
  } catch (err) {
    console.error('Questions GET error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
