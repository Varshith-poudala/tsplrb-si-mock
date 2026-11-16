'use client';

import { useState, useEffect } from 'react';
import { useSession } from 'next-auth/react';
import Navbar from '@/components/Navbar';
import Link from 'next/link';
import { 
  Trophy, Clock, CheckCircle2, XCircle, Award, RotateCcw, FileText, ChevronRight, 
  Lock, Crown, BarChart2, Play, Pause, BookOpen, Target, CheckCircle, Sparkles, 
  TrendingUp, AlertCircle, Compass, Zap, Shield, HelpCircle
} from 'lucide-react';

export default function DashboardPage() {
  const { data: session, status } = useSession();
  const [attempts, setAttempts] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [inProgressTests, setInProgressTests] = useState({});
  const [difficultyFilter, setDifficultyFilter] = useState('all'); // 'all' | 'Easy' | 'Medium' | 'Tough'

  useEffect(() => {
    try {
      const testIds = [
        'demo-test-50',
        'tsplrb-si-mock-full-200',
        'tsplrb-si-mock-full-200-2',
        'tsplrb-si-mock-full-200-3',
        'tsplrb-si-mock-full-200-4',
        'tsplrb-si-mock-full-200-5'
      ];
      const prog = {};
      testIds.forEach(id => {
        const stored = localStorage.getItem(`exam_progress_${id}`);
        if (stored) {
          const p = JSON.parse(stored);
          if (p.answers && Object.keys(p.answers).length > 0) prog[id] = p;
        }
      });
      setInProgressTests(prog);
    } catch (e) {}
  }, []);

  useEffect(() => {
    async function loadAttempts() {
      try {
        const res = await fetch('/api/attempts');
        const data = await res.json();
        setAttempts(data.attempts || []);
        setStats(data.stats || null);
      } catch (err) {
        console.error('Failed to load past attempts:', err);
      } finally {
        setLoading(false);
      }
    }

    if (session?.user) {
      loadAttempts();
    } else if (status !== 'loading') {
      setLoading(false);
    }
  }, [session, status]);

  const isAdmin = session?.user?.role === 'admin';
  const isPaid = session?.user?.isPaid || isAdmin;

  if (status === 'loading') {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex items-center justify-center transition-colors">
        <div className="w-8 h-8 border-3 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  if (!session?.user) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col transition-colors">
        <Navbar />
        <div className="flex-1 flex items-center justify-center p-4">
          <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-8 text-center shadow-lg">
            <div className="w-12 h-12 bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-amber-400 rounded-xl flex items-center justify-center mx-auto mb-4 border border-slate-200 dark:border-slate-700">
              <Trophy className="w-6 h-6" />
            </div>
            <h1 className="text-xl font-bold text-slate-900 dark:text-white mb-2">Sign In to View Dashboard</h1>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
              Track your scores, re-take mock tests multiple times, and view in-depth performance analytics.
            </p>
            <Link
              href="/login"
              className="inline-block w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl transition-colors text-xs shadow-xs"
            >
              Sign In to Continue
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const inProgressKeys = Object.keys(inProgressTests);

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col transition-colors">
      <Navbar />

      <main className="flex-1 max-w-[1440px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
        
        {/* 1. TOP CANDIDATE HERO BANNER (Wide & High-Density) */}
        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xs">
          <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-5">
            
            {/* Candidate Identity & Role */}
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-black text-lg flex items-center justify-center flex-shrink-0 shadow-xs">
                {(session.user.name || session.user.email || 'U').charAt(0).toUpperCase()}
              </div>
              <div>
                <div className="flex flex-wrap items-center gap-2 mb-1">
                  <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Candidate Dashboard</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
                    TSPLRB SI 2024-25 PWT
                  </span>
                  {isAdmin && (
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-purple-50 dark:bg-purple-950/60 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800">
                      Super Admin
                    </span>
                  )}
                </div>
                <h1 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
                  {session.user.name || session.user.email}
                </h1>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                  Preliminary Written Test (PWT) Preparation Hub • 200 Questions • 3 Hours • Bilingual (EN / తెలుగు)
                </p>
              </div>
            </div>

            {/* Access Badge & Key Specs */}
            <div className="flex flex-wrap items-center gap-3 w-full lg:w-auto justify-between lg:justify-end">
              <div className="hidden sm:flex items-center gap-3 text-xs bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl px-4 py-2.5">
                <div className="text-center">
                  <div className="text-[10px] text-slate-400 font-semibold uppercase">Exam Mode</div>
                  <div className="font-bold text-slate-800 dark:text-slate-200">Online CBT</div>
                </div>
                <div className="w-px h-6 bg-slate-200 dark:bg-slate-800" />
                <div className="text-center">
                  <div className="text-[10px] text-slate-400 font-semibold uppercase">Target Cut-Off</div>
                  <div className="font-bold text-emerald-600 dark:text-emerald-400">80/200 Marks</div>
                </div>
                <div className="w-px h-6 bg-slate-200 dark:bg-slate-800" />
                <div className="text-center">
                  <div className="text-[10px] text-slate-400 font-semibold uppercase">Negative Marking</div>
                  <div className="font-bold text-rose-600 dark:text-rose-400">-0.20 Marks</div>
                </div>
              </div>

              {isPaid ? (
                <div className="bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800 px-4 py-2.5 rounded-xl flex items-center gap-2.5 shadow-xs">
                  <Crown className="w-4 h-4 text-emerald-600 dark:text-amber-400 flex-shrink-0" />
                  <div>
                    <div className="text-xs font-bold text-emerald-800 dark:text-emerald-300">Full Access Active</div>
                    <div className="text-[10px] text-emerald-600 dark:text-emerald-400">All 200-question papers unlocked</div>
                  </div>
                </div>
              ) : (
                <div className="bg-slate-100 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 px-4 py-2 rounded-xl flex items-center gap-3">
                  <div>
                    <div className="text-xs font-bold text-slate-800 dark:text-slate-200">Free Demo Mode</div>
                    <div className="text-[10px] text-slate-500 dark:text-slate-400">Unlock all full papers for ₹99</div>
                  </div>
                  <Link
                    href="/#pricing"
                    className="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-3 py-1.5 rounded-lg transition-colors shadow-xs"
                  >
                    Unlock ₹99
                  </Link>
                </div>
              )}
            </div>

          </div>
        </div>

        {/* 2. MAIN 2-COLUMN GRID (8 COLS MAIN + 4 COLS SIDEBAR) */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 mt-6">
          
          {/* ================= LEFT MAIN COLUMN (8 Columns) ================= */}
          <div className="lg:col-span-8 space-y-6">
            
            {/* Active Test Resume Banner (If user has an unfinished test) */}
            {inProgressKeys.length > 0 && (
              <div className="bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800 rounded-2xl p-4 sm:p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-xs">
                <div className="flex items-center gap-3 text-amber-900 dark:text-amber-200">
                  <div className="w-10 h-10 rounded-xl bg-amber-100 dark:bg-amber-900/60 flex items-center justify-center flex-shrink-0">
                    <Pause className="w-5 h-5 text-amber-700 dark:text-amber-400 fill-current" />
                  </div>
                  <div>
                    <div className="text-xs font-bold flex items-center gap-2">
                      <span>Exam Session In Progress</span>
                      <span className="bg-amber-200 dark:bg-amber-800/80 text-amber-900 dark:text-amber-100 text-[10px] font-bold px-2 py-0.2 rounded-full">
                        Saved in Browser
                      </span>
                    </div>
                    <div className="text-xs text-amber-800 dark:text-amber-300 mt-0.5">
                      {inProgressKeys[0] === 'demo-test-50' ? 'TSPLRB SI Free Demo Mock Test' : 'TSPLRB SI Mock Test 1 (Full 200 Qs)'} • {Object.keys(inProgressTests[inProgressKeys[0]]?.answers || {}).length} questions answered
                    </div>
                  </div>
                </div>

                <Link
                  href={`/exam/${inProgressKeys[0]}`}
                  className="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs px-4 py-2 rounded-xl transition-colors shadow-xs flex items-center gap-1.5 flex-shrink-0"
                >
                  <Play className="w-3.5 h-3.5 fill-current" />
                  <span>Resume Test Now</span>
                </Link>
              </div>
            )}

            {/* Available Mock Tests Section */}
            <div>
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3.5">
                <div>
                  <h2 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                    <BookOpen className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                    Available Mock Test Papers (6 Papers)
                  </h2>
                  <p className="text-xs text-slate-500 dark:text-slate-400">Full 200-Question CBT papers categorized by difficulty: Easy, Medium, and Tough</p>
                </div>

                {/* Difficulty Filter Tabs */}
                <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-900 p-1 rounded-xl border border-slate-200 dark:border-slate-800">
                  {['all', 'Easy', 'Medium', 'Tough'].map((level) => {
                    const count = level === 'all'
                      ? [
                          'demo-test-50',
                          'tsplrb-si-mock-full-200-3',
                          'tsplrb-si-mock-full-200',
                          'tsplrb-si-mock-full-200-2',
                          'tsplrb-si-mock-full-200-4',
                          'tsplrb-si-mock-full-200-5'
                        ].length
                      : level === 'Easy' ? 2 : level === 'Medium' ? 3 : 1;
                    return (
                      <button
                        key={level}
                        onClick={() => setDifficultyFilter(level)}
                        className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all cursor-pointer flex items-center gap-1 ${
                          difficultyFilter === level
                            ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs'
                            : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'
                        }`}
                      >
                        <span>{level === 'all' ? 'All' : level}</span>
                        <span className="opacity-70 text-[10px]">({count})</span>
                      </button>
                    );
                  })}
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {[
                  {
                    testId: 'demo-test-50',
                    title: 'TSPLRB SI Free Demo Mock Test',
                    difficulty: 'Easy',
                    badge: 'FREE DEMO',
                    questions: 50,
                    duration: '45 Mins',
                    marks: 50,
                    isFree: true,
                    description: 'Benchmark diagnostic paper: 15 Arithmetic + 15 Reasoning + 20 General Studies & Telangana with official -0.20 negative marking.',
                  },
                  {
                    testId: 'tsplrb-si-mock-full-200-3',
                    title: 'TSPLRB SI Mock Test 3 (Easy • Foundational PWT)',
                    difficulty: 'Easy',
                    badge: 'EASY • FOUNDATIONAL',
                    questions: 200,
                    duration: '180 Mins (3 Hrs)',
                    marks: 200,
                    isFree: false,
                    description: 'Foundational 200Q full paper focusing on core formulas, direct arithmetic calculations, clear reasoning, and essential General Studies facts.',
                  },
                  {
                    testId: 'tsplrb-si-mock-full-200',
                    title: 'TSPLRB SI Mock Test 1 (Official Blueprint)',
                    difficulty: 'Medium',
                    badge: 'OFFICIAL FULL-LENGTH',
                    questions: 200,
                    duration: '180 Mins (3 Hrs)',
                    marks: 200,
                    isFree: false,
                    description: 'Official 200Q blueprint: 50 Arithmetic + 50 Reasoning + 100 General Studies & Telangana Movement (1948–2014) with balanced time pressure.',
                  },
                  {
                    testId: 'tsplrb-si-mock-full-200-2',
                    title: 'TSPLRB SI Mock Test 2 (High Yield Practice)',
                    difficulty: 'Medium',
                    badge: 'HIGH YIELD',
                    questions: 200,
                    duration: '180 Mins (3 Hrs)',
                    marks: 200,
                    isFree: false,
                    description: 'Standard practice paper with high weightage on Telangana State schemes, constitutional governance, culture, and reasoning series.',
                  },
                  {
                    testId: 'tsplrb-si-mock-full-200-4',
                    title: 'TSPLRB SI Mock Test 4 (Medium • Official Standard PWT)',
                    difficulty: 'Medium',
                    badge: 'MEDIUM • 2022 PYQ STANDARD',
                    questions: 200,
                    duration: '180 Mins (3 Hrs)',
                    marks: 200,
                    isFree: false,
                    description: 'Exact replica of official TSPLRB SI 2022 Prelims. Multi-step word problems, logical reasoning, and official Telangana Movement history.',
                  },
                  {
                    testId: 'tsplrb-si-mock-full-200-5',
                    title: 'TSPLRB SI Mock Test 5 (Tough • Advanced High-Yield PWT)',
                    difficulty: 'Tough',
                    badge: 'TOUGH • ADVANCED SIMULATION',
                    questions: 200,
                    duration: '180 Mins (3 Hrs)',
                    marks: 200,
                    isFree: false,
                    description: 'High-difficulty 200Q simulation modeling recent TSPSC and TSPLRB trends. Advanced statement-based questions and intricate puzzles.',
                  },
                ]
                  .filter(t => difficultyFilter === 'all' || t.difficulty.toLowerCase() === difficultyFilter.toLowerCase())
                  .map((test) => {
                    const hasProgress = inProgressTests[test.testId];
                    const isUnlocked = test.isFree || isPaid;

                    let badgeClasses = 'bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border-blue-200 dark:border-blue-800';
                    if (test.difficulty === 'Easy') badgeClasses = 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800';
                    else if (test.difficulty === 'Tough') badgeClasses = 'bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800';

                    return (
                      <div key={test.testId} className={`bg-white dark:bg-slate-900 border rounded-xl p-5 transition-colors flex flex-col justify-between shadow-xs ${
                        isUnlocked ? 'border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700' : 'border-slate-200 dark:border-slate-800/80'
                      }`}>
                        <div>
                          <div className="flex items-center justify-between mb-2">
                            <div className="flex items-center gap-1.5">
                              <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${badgeClasses}`}>
                                {test.badge}
                              </span>
                              <span className="text-[10px] font-semibold text-slate-500 dark:text-slate-400 bg-slate-100 dark:bg-slate-800 px-2 py-0.5 rounded-md">
                                {test.difficulty}
                              </span>
                            </div>
                            <span className="text-[11px] text-slate-400 font-medium">{test.questions} Qs • {test.duration}</span>
                          </div>
                          <h3 className="font-bold text-slate-900 dark:text-white text-sm">{test.title}</h3>
                          <p className="text-xs text-slate-600 dark:text-slate-400 mt-1.5 leading-relaxed">
                            {test.description}
                          </p>
                        </div>

                        <div className="mt-5 pt-3.5 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                          <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">
                            {hasProgress ? `${Object.keys(hasProgress.answers || {}).length}/${test.questions} Answered` : `${test.marks} Marks`}
                          </span>

                          {hasProgress ? (
                            <Link
                              href={`/exam/${test.testId}`}
                              className="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs px-3.5 py-1.5 rounded-lg transition-colors shadow-xs flex items-center gap-1.5"
                            >
                              <Play className="w-3.5 h-3.5 fill-current" />
                              <span>Resume Exam</span>
                            </Link>
                          ) : isUnlocked ? (
                            <Link
                              href={`/exam/${test.testId}`}
                              className={`font-bold text-xs px-3.5 py-1.5 rounded-lg transition-colors shadow-xs flex items-center gap-1 ${
                                test.isFree
                                  ? 'bg-blue-600 hover:bg-blue-700 text-white'
                                  : 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100'
                              }`}
                            >
                              <span>Start Exam</span>
                              <ChevronRight className="w-3.5 h-3.5" />
                            </Link>
                          ) : (
                            <Link
                              href="/#pricing"
                              className="bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-200 font-semibold text-xs px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1"
                            >
                              <Lock className="w-3.5 h-3.5 text-slate-500" />
                              <span>Unlock ₹99</span>
                            </Link>
                          )}
                        </div>
                      </div>
                    );
                  })}
              </div>
            </div>

            {/* Previous Results & Attempt History Table (or Motivating Roadmap if empty) */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl overflow-hidden shadow-xs">
              <div className="p-4 sm:p-5 border-b border-slate-100 dark:border-slate-800 flex items-center justify-between">
                <div>
                  <h2 className="text-sm sm:text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                    <FileText className="w-4 h-4 text-blue-600 dark:text-amber-400" />
                    Previous Results & Attempt History
                  </h2>
                  <p className="text-xs text-slate-500 dark:text-slate-400">Review your past scores, accuracy breakdown, and official solutions</p>
                </div>
                <span className="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-bold px-2.5 py-1 rounded-lg border border-slate-200 dark:border-slate-700">
                  {attempts.length} Total Attempts
                </span>
              </div>

              {loading ? (
                <div className="p-8 text-center text-slate-500">
                  <div className="w-6 h-6 border-2 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto mb-2"></div>
                  <span className="text-xs">Loading performance data...</span>
                </div>
              ) : attempts.length === 0 ? (
                /* Rich 3-Step Strategy Card instead of empty space */
                <div className="p-6">
                  <div className="bg-slate-50 dark:bg-slate-950/80 border border-slate-200 dark:border-slate-800/80 rounded-xl p-5">
                    <div className="flex items-center gap-2 text-xs font-bold text-slate-900 dark:text-white mb-2">
                      <Sparkles className="w-4 h-4 text-amber-500" />
                      <span>Kickstart Your TSPLRB SI Preparation (3-Step Roadmap)</span>
                    </div>
                    <p className="text-xs text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">
                      You haven't submitted any test attempts yet. Candidates who take at least 3 full-length simulations score an average of 28 marks higher in the final PWT:
                    </p>

                    <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-5">
                      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-3">
                        <div className="text-[10px] font-bold text-blue-600 dark:text-blue-400 mb-1">STEP 1 • 45 MINS</div>
                        <div className="text-xs font-bold text-slate-800 dark:text-slate-200">Free 50-Q Demo Test</div>
                        <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">Assess baseline speed in Arithmetic, Reasoning & GS.</div>
                      </div>

                      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-3">
                        <div className="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 mb-1">STEP 2 • 3 HOURS</div>
                        <div className="text-xs font-bold text-slate-800 dark:text-slate-200">Full 200Q Simulation</div>
                        <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">Practice endurance & target 70%+ accuracy with -0.20 penalty.</div>
                      </div>

                      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-3">
                        <div className="text-[10px] font-bold text-purple-600 dark:text-purple-400 mb-1">STEP 3 • ANALYSIS</div>
                        <div className="text-xs font-bold text-slate-800 dark:text-slate-200">Bilingual Solutions</div>
                        <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">Review official English & Telugu rationales for all questions.</div>
                      </div>
                    </div>

                    <Link
                      href="/exam/demo-test-50"
                      className="inline-flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs px-4 py-2 rounded-xl transition-colors shadow-xs"
                    >
                      <Play className="w-3.5 h-3.5 fill-current" />
                      <span>Take Free Demo Test (50 Questions)</span>
                    </Link>
                  </div>
                </div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full text-left text-xs text-slate-700 dark:text-slate-300">
                    <thead className="bg-slate-50 dark:bg-slate-950/60 text-slate-500 dark:text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-200 dark:border-slate-800">
                      <tr>
                        <th className="py-3 px-4">Test Name</th>
                        <th className="py-3 px-4">Attempt</th>
                        <th className="py-3 px-4">Date</th>
                        <th className="py-3 px-4">Score</th>
                        <th className="py-3 px-4">Accuracy</th>
                        <th className="py-3 px-4">Correct / Wrong</th>
                        <th className="py-3 px-4 text-right">Actions</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100 dark:divide-slate-800">
                      {attempts.map((att) => {
                        const testLabel = att.testId?.includes('demo') ? '50-Q Free Demo Mock' : 'Full 200-Q Mock Test 1';
                        return (
                          <tr key={att.id} className="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors">
                            <td className="py-3.5 px-4 font-semibold text-slate-900 dark:text-white">
                              {testLabel}
                            </td>
                            <td className="py-3.5 px-4">
                              <span className="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 px-2 py-0.5 rounded text-[10px] font-semibold border border-slate-200 dark:border-slate-700">
                                Attempt #{att.attemptNumber || 1}
                              </span>
                            </td>
                            <td className="py-3.5 px-4 text-slate-500 dark:text-slate-400">
                              {new Date(att.submittedAt).toLocaleDateString('en-IN', {
                                day: 'numeric',
                                month: 'short',
                                year: 'numeric',
                              })}
                            </td>
                            <td className="py-3.5 px-4 font-bold text-slate-900 dark:text-amber-400 text-sm">
                              {att.totalScore} <span className="text-[10px] text-slate-400 font-normal">/ {att.totalMarks}</span>
                            </td>
                            <td className="py-3.5 px-4 font-semibold text-emerald-600 dark:text-emerald-400">
                              {att.accuracyPercent}%
                            </td>
                            <td className="py-3.5 px-4">
                              <span className="text-emerald-600 dark:text-emerald-400 font-bold">{att.correctCount} ✓</span>
                              <span className="text-slate-400 mx-1">/</span>
                              <span className="text-rose-600 dark:text-rose-400 font-bold">{att.wrongCount} ✗</span>
                            </td>
                            <td className="py-3.5 px-4 text-right">
                              <Link
                                href={`/exam/${att.testId}`}
                                className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 border border-slate-200 dark:border-slate-700 px-2.5 py-1 rounded-md text-[11px] font-semibold transition-colors"
                              >
                                Retake Test
                              </Link>
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              )}
            </div>

          </div>

          {/* ================= RIGHT SIDEBAR COLUMN (4 Columns) ================= */}
          <div className="lg:col-span-4 space-y-6">
            
            {/* Performance Overview (Compact 2x2 Grid) */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 shadow-xs">
              <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-100 dark:border-slate-800">
                <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
                  <BarChart2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                  Performance Overview
                </h3>
                <span className="text-[10px] font-semibold text-slate-400">Live Analytics</span>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="bg-slate-50 dark:bg-slate-950 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Attempts Taken</div>
                  <div className="text-xl font-black text-slate-900 dark:text-white mt-1">
                    {stats?.totalAttempts || 0}
                  </div>
                  <div className="text-[9px] text-slate-400 mt-0.5">Unlimited retakes</div>
                </div>

                <div className="bg-slate-50 dark:bg-slate-950 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Best Score</div>
                  <div className="text-xl font-black text-slate-900 dark:text-amber-400 mt-1">
                    {stats?.bestScore !== undefined ? `${stats.bestScore}` : '—'}
                  </div>
                  <div className="text-[9px] text-slate-400 mt-0.5">Out of 200 marks</div>
                </div>

                <div className="bg-slate-50 dark:bg-slate-950 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Average Score</div>
                  <div className="text-xl font-black text-purple-600 dark:text-purple-300 mt-1">
                    {stats?.averageScore !== undefined ? `${stats.averageScore}` : '—'}
                  </div>
                  <div className="text-[9px] text-slate-400 mt-0.5">Across all tests</div>
                </div>

                <div className="bg-slate-50 dark:bg-slate-950 p-3 rounded-xl border border-slate-100 dark:border-slate-800">
                  <div className="text-[10px] text-slate-500 dark:text-slate-400 font-medium">Accuracy</div>
                  <div className="text-xl font-black text-emerald-600 dark:text-emerald-400 mt-1">
                    {stats?.averageAccuracy !== undefined ? `${stats.averageAccuracy}%` : '—'}
                  </div>
                  <div className="text-[9px] text-slate-400 mt-0.5">Target &gt; 70%</div>
                </div>
              </div>
            </div>

            {/* Official TSPLRB SI Exam Pattern Blueprint */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 shadow-xs">
              <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5 mb-3">
                <Target className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                PWT Exam Pattern & Cut-Offs
              </h3>

              <div className="space-y-2 text-xs">
                <div className="flex items-center justify-between p-2 rounded-lg bg-slate-50 dark:bg-slate-950 border border-slate-100 dark:border-slate-800">
                  <span className="font-medium text-slate-700 dark:text-slate-300">Total Questions</span>
                  <span className="font-bold text-slate-900 dark:text-white">200 Questions</span>
                </div>
                <div className="flex items-center justify-between p-2 rounded-lg bg-slate-50 dark:bg-slate-950 border border-slate-100 dark:border-slate-800">
                  <span className="font-medium text-slate-700 dark:text-slate-300">Total Marks</span>
                  <span className="font-bold text-slate-900 dark:text-white">200 Marks</span>
                </div>
                <div className="flex items-center justify-between p-2 rounded-lg bg-slate-50 dark:bg-slate-950 border border-slate-100 dark:border-slate-800">
                  <span className="font-medium text-slate-700 dark:text-slate-300">Exam Duration</span>
                  <span className="font-bold text-slate-900 dark:text-white">3 Hours (180 mins)</span>
                </div>
                <div className="flex items-center justify-between p-2 rounded-lg bg-slate-50 dark:bg-slate-950 border border-slate-100 dark:border-slate-800">
                  <span className="font-medium text-slate-700 dark:text-slate-300">Negative Penalty</span>
                  <span className="font-bold text-rose-600 dark:text-rose-400">-0.20 Marks (1/5th)</span>
                </div>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800">
                <div className="text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-1.5">Official Minimum Qualifying Marks:</div>
                <div className="grid grid-cols-3 gap-1.5 text-center text-[10px]">
                  <div className="bg-slate-50 dark:bg-slate-950 p-1.5 rounded border border-slate-200 dark:border-slate-800">
                    <div className="text-slate-400">OC (40%)</div>
                    <div className="font-bold text-slate-900 dark:text-white mt-0.5">80 Marks</div>
                  </div>
                  <div className="bg-slate-50 dark:bg-slate-950 p-1.5 rounded border border-slate-200 dark:border-slate-800">
                    <div className="text-slate-400">BC (35%)</div>
                    <div className="font-bold text-slate-900 dark:text-white mt-0.5">70 Marks</div>
                  </div>
                  <div className="bg-slate-50 dark:bg-slate-950 p-1.5 rounded border border-slate-200 dark:border-slate-800">
                    <div className="text-slate-400">SC/ST (30%)</div>
                    <div className="font-bold text-slate-900 dark:text-white mt-0.5">60 Marks</div>
                  </div>
                </div>
              </div>
            </div>

            {/* High-Yield Subject Weightage */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 shadow-xs">
              <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5 mb-3">
                <Compass className="w-4 h-4 text-purple-600 dark:text-purple-400" />
                Syllabus & Weightage Breakdown
              </h3>

              <div className="space-y-3 text-xs">
                <div>
                  <div className="flex items-center justify-between text-xs font-semibold mb-1">
                    <span className="text-slate-700 dark:text-slate-300">Arithmetic (50 Qs • 25%)</span>
                    <span className="text-blue-600 font-bold">50 Marks</span>
                  </div>
                  <div className="w-full bg-slate-100 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div className="bg-blue-600 h-full rounded-full" style={{ width: '25%' }} />
                  </div>
                  <p className="text-[10px] text-slate-400 mt-1">Number System, Percentages, SI/CI, Time & Work, Mensuration</p>
                </div>

                <div>
                  <div className="flex items-center justify-between text-xs font-semibold mb-1">
                    <span className="text-slate-700 dark:text-slate-300">Reasoning Ability (50 Qs • 25%)</span>
                    <span className="text-purple-600 font-bold">50 Marks</span>
                  </div>
                  <div className="w-full bg-slate-100 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div className="bg-purple-600 h-full rounded-full" style={{ width: '25%' }} />
                  </div>
                  <p className="text-[10px] text-slate-400 mt-1">Syllogisms, Blood Relations, Coding, Series, Non-Verbal</p>
                </div>

                <div>
                  <div className="flex items-center justify-between text-xs font-semibold mb-1">
                    <span className="text-slate-700 dark:text-slate-300">General Studies (100 Qs • 50%)</span>
                    <span className="text-emerald-600 font-bold">100 Marks</span>
                  </div>
                  <div className="w-full bg-slate-100 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div className="bg-emerald-600 h-full rounded-full" style={{ width: '50%' }} />
                  </div>
                  <p className="text-[10px] text-slate-400 mt-1">Telangana Movement & Statehood, Indian Constitution, History, Geography, Current Affairs</p>
                </div>
              </div>
            </div>

            {/* CBT Exam Navigation Tips */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 shadow-xs">
              <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5 mb-2.5">
                <Zap className="w-4 h-4 text-amber-500" />
                CBT Navigation & Time Tips
              </h3>
              <ul className="space-y-2 text-xs text-slate-600 dark:text-slate-400">
                <li className="flex items-start gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-blue-600 mt-1.5 flex-shrink-0" />
                  <span><strong>10 Qs Per Page</strong>: Scroll through 10 questions at a time or use Section Pills to jump directly to Q1, Q51, or Q101.</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-600 mt-1.5 flex-shrink-0" />
                  <span><strong>Live Question Palette</strong>: Green = Answered, Red = Not Answered, Purple = Marked for Review.</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="w-1.5 h-1.5 rounded-full bg-amber-500 mt-1.5 flex-shrink-0" />
                  <span><strong>Pacing Strategy</strong>: Spend ~40s on GS questions and save 75s–90s for Arithmetic calculations.</span>
                </li>
              </ul>
            </div>

          </div>

        </div>

      </main>
    </div>
  );
}