import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import connectToDatabase from '@/lib/mongodb';
import Attempt from '@/models/Attempt';
import User from '@/models/User';

export const dynamic = 'force-dynamic';

export async function GET(req) {
  try {
    const session = await getServerSession(authOptions);

    if (!session?.user?.email) {
      return NextResponse.json({ attempts: [], stats: null });
    }

    const conn = await connectToDatabase();
    if (!conn) {
      return NextResponse.json({
        attempts: [],
        stats: { totalAttempts: 0, bestScore: 0, averageScore: 0, averageAccuracy: 0 }
      });
    }

    const userEmail = session.user.email.toLowerCase();

    const attempts = await Attempt.find({ userEmail })
      .sort({ createdAt: -1 })
      .lean();

    if (!attempts || attempts.length === 0) {
      return NextResponse.json({
        attempts: [],
        stats: {
          totalAttempts: 0,
          bestScore: 0,
          averageScore: 0,
          averageAccuracy: 0,
        }
      });
    }

    const totalAttempts = attempts.length;
    const scores = attempts.map(a => a.totalScore);
    const bestScore = Math.max(...scores);
    const averageScore = parseFloat((scores.reduce((a, b) => a + b, 0) / totalAttempts).toFixed(2));
    const averageAccuracy = parseFloat((attempts.reduce((a, b) => a + (b.accuracyPercent || 0), 0) / totalAttempts).toFixed(1));

    return NextResponse.json({
      attempts: attempts.map(a => ({
        id: a._id.toString(),
        testId: a.testId,
        attemptNumber: a.attemptNumber,
        totalScore: a.totalScore,
        totalMarks: a.totalMarks,
        correctCount: a.correctCount,
        wrongCount: a.wrongCount,
        unansweredCount: a.unansweredCount,
        accuracyPercent: a.accuracyPercent,
        durationSeconds: a.durationSeconds,
        sectionScores: a.sectionScores,
        submittedAt: a.submittedAt,
      })),
      stats: {
        totalAttempts,
        bestScore,
        averageScore,
        averageAccuracy,
      }
    });
  } catch (err) {
    console.error('Attempts GET error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}
