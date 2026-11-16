import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import User from '@/models/User';
import Attempt from '@/models/Attempt';
import fs from 'fs';
import path from 'path';

export async function POST(req, { params }) {
  try {
    const { id } = params;
    const body = await req.json();
    const { answers = {}, startedAt, durationSeconds = 0 } = body;

    const session = await getServerSession(authOptions);
    const userEmail = session?.user?.email || 'guest_demo@tsplrb.com';

    // 1. Load Master Question Bank (with correct answers & explanations)
    let fileName = 'mock_test_full_200.json';
    if (id === 'tsplrb-si-mock-full-200-3') fileName = 'mock_test_full_200_3.json';
    else if (id === 'tsplrb-si-mock-full-200-4') fileName = 'mock_test_full_200_4.json';
    else if (id === 'tsplrb-si-mock-full-200-5') fileName = 'mock_test_full_200_5.json';

    const localFilePath = path.join(process.cwd(), 'public/data', fileName);
    let masterQuestions = [];

    if (fs.existsSync(localFilePath)) {
      const fileContent = fs.readFileSync(localFilePath, 'utf-8');
      const parsed = JSON.parse(fileContent);
      masterQuestions = parsed.questions || [];
    }

    const isDemo = id === 'demo-test-50';
    if (isDemo && masterQuestions.length > 50) {
      const arith = masterQuestions.slice(0, 20);
      const reasoning = masterQuestions.slice(50, 65);
      const gs = masterQuestions.slice(100, 115);
      masterQuestions = [...arith, ...reasoning, ...gs].map((q, idx) => ({
        ...q,
        id: idx + 1,
        qNumber: idx + 1,
      }));
    }

    // 2. Server-Side Scoring Calculation
    let correctCount = 0;
    let wrongCount = 0;
    let unansweredCount = 0;
    let totalScore = 0.0;

    const sectionBreakdown = {
      arithmetic: { name: 'Part A: Arithmetic', total: 0, correct: 0, wrong: 0, score: 0 },
      reasoning: { name: 'Part B: Reasoning', total: 0, correct: 0, wrong: 0, score: 0 },
      generalStudies: { name: 'Part C: General Studies', total: 0, correct: 0, wrong: 0, score: 0 },
    };

    const reviewQuestions = masterQuestions.map((q) => {
      const qNum = q.id || q.qNumber;
      const selected = answers[qNum] !== undefined && answers[qNum] !== null ? Number(answers[qNum]) : null;
      const correct = Number(q.correct_option);

      let secKey = 'generalStudies';
      if (q.section?.toLowerCase().includes('arithmetic')) secKey = 'arithmetic';
      else if (q.section?.toLowerCase().includes('reasoning')) secKey = 'reasoning';

      sectionBreakdown[secKey].total += 1;

      let isCorrect = false;

      if (selected === null || selected === -1) {
        unansweredCount += 1;
      } else if (selected === correct) {
        correctCount += 1;
        isCorrect = true;
        totalScore += 1.0;
        sectionBreakdown[secKey].correct += 1;
        sectionBreakdown[secKey].score += 1.0;
      } else {
        wrongCount += 1;
        totalScore -= 0.20;
        sectionBreakdown[secKey].wrong += 1;
        sectionBreakdown[secKey].score -= 0.20;
      }

      // Return question with solution now that test is finished!
      return {
        id: qNum,
        qNumber: qNum,
        section: q.section,
        topic: q.topic || '',
        question_en: q.question_en,
        question_te: q.question_te,
        options_en: q.options_en,
        options_te: q.options_te,
        userSelectedOption: selected,
        correct_option: correct,
        isCorrect,
        explanation_en: q.explanation_en,
        explanation_te: q.explanation_te,
      };
    });

    // Round scores
    totalScore = Math.max(0, parseFloat(totalScore.toFixed(2)));
    Object.keys(sectionBreakdown).forEach(k => {
      sectionBreakdown[k].score = parseFloat(sectionBreakdown[k].score.toFixed(2));
    });

    const attemptedCount = correctCount + wrongCount;
    const accuracyPercent = attemptedCount > 0 ? parseFloat(((correctCount / attemptedCount) * 100).toFixed(1)) : 0;

    // 3. Save Attempt to MongoDB (Supports multiple attempts & history!)
    let attemptRecord = null;
    try {
      const conn = await connectToDatabase();
      if (conn) {
        let dbUser = await User.findOne({ email: userEmail.toLowerCase() });

        if (!dbUser && session?.user?.email) {
          dbUser = await User.create({
            email: userEmail.toLowerCase(),
            name: session.user.name || 'Candidate',
            role: 'user',
            isPaid: false,
          });
        }

        if (dbUser) {
          const previousAttempts = await Attempt.countDocuments({
            userId: dbUser._id,
            testId: id,
          });

          attemptRecord = await Attempt.create({
            userId: dbUser._id,
            userEmail: dbUser.email,
            testId: id,
            attemptNumber: previousAttempts + 1,
            startedAt: startedAt ? new Date(startedAt) : new Date(Date.now() - durationSeconds * 1000),
            submittedAt: new Date(),
            durationSeconds: durationSeconds || 0,
            totalScore,
            totalMarks: masterQuestions.length,
            correctCount,
            wrongCount,
            unansweredCount,
            accuracyPercent,
            sectionScores: sectionBreakdown,
            answers: reviewQuestions.map(r => ({
              qNumber: r.qNumber,
              selectedOption: r.userSelectedOption,
              isCorrect: r.isCorrect,
              correctOption: r.correct_option,
            })),
          });
        }
      }
    } catch (dbErr) {
      console.warn('Could not persist attempt to MongoDB:', dbErr.message);
    }

    return NextResponse.json({
      success: true,
      attemptId: attemptRecord?._id || 'local_session',
      attemptNumber: attemptRecord?.attemptNumber || 1,
      totalScore,
      totalMarks: masterQuestions.length,
      correctCount,
      wrongCount,
      unansweredCount,
      accuracyPercent,
      durationSeconds,
      sectionBreakdown,
      reviewQuestions,
    });
  } catch (err) {
    console.error('Submit evaluation error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
