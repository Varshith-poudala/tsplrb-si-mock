import React, { useState, useEffect } from 'react';
import { Link, useSearchParams, useNavigate } from 'react-router-dom';
import { 
  Trophy, Clock, CheckCircle2, XCircle, Award, RotateCcw, FileText, ChevronRight, 
  Lock, Crown, BarChart2, Play, Pause, BookOpen, Target, CheckCircle, Sparkles, 
  TrendingUp, AlertCircle, Compass, Zap, Shield, HelpCircle, Layers, X, ExternalLink,
  LayoutDashboard
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { getExamProgressKey, ALL_TEST_IDS } from '../utils/storage';
import CheckoutModal from '../components/CheckoutModal';

// Helper component for category breakdown popover on hover
function CategoryHoverCard({ title, items, openDown = false }) {
  return (
    <div className={`absolute ${openDown ? 'top-full mt-2' : 'bottom-full mb-2'} left-1/2 -translate-x-1/2 hidden group-hover:block z-50 w-64 p-3 bg-slate-900 text-white rounded-xl shadow-2xl border border-slate-700 text-left pointer-events-none animate-in fade-in duration-150`}>
      <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-2 border-b border-slate-800 pb-1.5 flex items-center justify-between">
        <span>{title}</span>
      </div>
      <div className="space-y-1.5 text-xs">
        {items.map((item, idx) => (
          <div key={idx} className="flex items-center justify-between">
            <span className="text-slate-300 text-[11px] font-medium">{item.label}</span>
            <span className={`font-mono font-bold text-[11px] ${item.color || 'text-white'}`}>{item.value}</span>
          </div>
        ))}
      </div>
      <div className={`absolute ${openDown ? '-top-1 border-b-slate-900 border-t-transparent' : 'top-full -mt-1 border-t-slate-900 border-b-transparent'} left-1/2 -translate-x-1/2 border-4 border-transparent`}></div>
    </div>
  );
}

// Format duration into clean human-readable string (e.g. 28s, 1m 24s, 1h 12m)
const formatDuration = (secs = 0) => {
  const s = Math.max(0, Math.round(Number(secs) || 0));
  const m = Math.floor(s / 60);
  const remS = s % 60;
  if (m >= 60) {
    const h = Math.floor(m / 60);
    const remM = m % 60;
    return `${h}h ${remM}m ${remS}s`;
  }
  if (m === 0) return `${remS}s`;
  return `${m}m ${remS}s`;
};

// Robust helper to extract or compute category-wise metrics for any attempt
function getAttemptCategoryMetrics(att) {
  const isDemo = att.testId?.includes('demo') || (att.totalMarks || 200) === 50;
  const maxArith = isDemo ? 15 : 50;
  const maxReason = isDemo ? 15 : 50;
  const maxGen = isDemo ? 20 : 100;

  // 1. Normalize raw section scores whether stored as Array, Object with sub-objects, or Object with numbers
  let rawSecs = [];
  if (Array.isArray(att.sectionScores) && att.sectionScores.length > 0) {
    rawSecs = att.sectionScores;
  } else if (att.sectionScores && typeof att.sectionScores === 'object') {
    const obj = att.sectionScores;
    Object.keys(obj).forEach(key => {
      const val = obj[key];
      if (typeof val === 'object' && val !== null) {
        rawSecs.push({ sectionKey: key, ...val });
      } else {
        rawSecs.push({ sectionKey: key, score: Number(val || 0) });
      }
    });
  }

  // 2. Lookup matching section by key or name
  const findSec = (key) => {
    return rawSecs.find(s => {
      if (s.sectionKey === key) return true;
      const name = (s.sectionName || '').toLowerCase();
      if (key === 'arithmetic') return name.includes('arith');
      if (key === 'reasoning') return name.includes('reason') || name.includes('mental');
      if (key === 'general') return name.includes('general') || name.includes('telangana') || name.includes('studies');
      return false;
    });
  };

  const recArith = findSec('arithmetic');
  const recReason = findSec('reasoning');
  const recGen = findSec('general');

  // If section records exist
  if (recArith || recReason || recGen) {
    const parse = (sec, defMax) => {
      const score = Number(sec?.score ?? sec?.marksObtained ?? 0);
      const rawTotal = Number(sec?.total ?? sec?.maxMarks ?? defMax);
      const total = rawTotal > 0 && !(rawTotal === 50 && defMax === 100) ? rawTotal : defMax;
      const correct = Number(sec?.correct ?? sec?.correctCount ?? 0);
      const wrong = Number(sec?.wrong ?? sec?.wrongCount ?? 0);
      const time = Number(sec?.timeSpentSeconds ?? sec?.time ?? 0);
      const attempted = correct + wrong;
      const accuracy = sec?.accuracyPercent !== undefined 
        ? Number(sec.accuracyPercent)
        : (attempted > 0 ? Math.round((correct / attempted) * 100) : 0);

      return {
        score: score.toFixed(1),
        maxMarks: total,
        correct,
        wrong,
        accuracy,
        time,
      };
    };

    const parsedArith = parse(recArith, maxArith);
    const parsedReason = parse(recReason, maxReason);
    const parsedGen = parse(recGen, maxGen);

    // If section times were not recorded (total 0s) but overall test duration > 0:
    // Distribute time ONLY to the sections where the candidate actually answered questions!
    const totalRecordedSecTime = parsedArith.time + parsedReason.time + parsedGen.time;
    const totalDuration = Number(att.durationSeconds || 0);

    if (totalRecordedSecTime === 0 && totalDuration > 0) {
      const arithAtt = parsedArith.correct + parsedArith.wrong;
      const reasonAtt = parsedReason.correct + parsedReason.wrong;
      const genAtt = parsedGen.correct + parsedGen.wrong;

      if (arithAtt > 0 && reasonAtt === 0 && genAtt === 0) {
        // Candidate only attempted Arithmetic (e.g. Page 1)
        parsedArith.time = totalDuration;
        parsedReason.time = 0;
        parsedGen.time = 0;
      } else if (reasonAtt > 0 && arithAtt === 0 && genAtt === 0) {
        parsedArith.time = 0;
        parsedReason.time = totalDuration;
        parsedGen.time = 0;
      } else if (genAtt > 0 && arithAtt === 0 && reasonAtt === 0) {
        parsedArith.time = 0;
        parsedReason.time = 0;
        parsedGen.time = totalDuration;
      } else if (arithAtt + reasonAtt + genAtt > 0) {
        const totalAtt = arithAtt + reasonAtt + genAtt;
        const tA = Math.round(totalDuration * (arithAtt / totalAtt));
        const tR = Math.round(totalDuration * (reasonAtt / totalAtt));
        const tG = Math.max(0, totalDuration - tA - tR);
        parsedArith.time = tA;
        parsedReason.time = tR;
        parsedGen.time = tG;
      } else {
        // 0 attempted questions, attribute time to arithmetic where test starts
        parsedArith.time = totalDuration;
        parsedReason.time = 0;
        parsedGen.time = 0;
      }
    }

    return {
      arithmetic: parsedArith,
      reasoning: parsedReason,
      general: parsedGen,
    };
  }

  // 3. True legacy fallback where no section data existed at all:
  const totalCorrect = Number(att.correctCount || 0);
  const totalWrong = Number(att.wrongCount || 0);
  const totalDuration = Number(att.durationSeconds || 0);
  const totalAtt = totalCorrect + totalWrong;
  const overallAcc = totalAtt > 0 ? Math.round((totalCorrect / totalAtt) * 100) : 0;

  // In TSPLRB CBT, exams begin at Q1 with Arithmetic.
  // If the candidate only answered a small number of questions (<= maxArith), all attempts occurred in Arithmetic!
  if (totalAtt <= maxArith) {
    return {
      arithmetic: {
        score: Number(att.totalScore || 0).toFixed(1),
        maxMarks: maxArith,
        correct: totalCorrect,
        wrong: totalWrong,
        accuracy: overallAcc,
        time: totalDuration,
      },
      reasoning: {
        score: '0.0',
        maxMarks: maxReason,
        correct: 0,
        wrong: 0,
        accuracy: 0,
        time: 0,
      },
      general: {
        score: '0.0',
        maxMarks: maxGen,
        correct: 0,
        wrong: 0,
        accuracy: 0,
        time: 0,
      },
    };
  }

  // If candidate answered more than maxArith questions across multiple sections:
  const arithC = Math.min(totalCorrect, maxArith);
  const remC1 = totalCorrect - arithC;
  const reasonC = Math.min(remC1, maxReason);
  const genC = remC1 - reasonC;

  const arithW = Math.min(totalWrong, Math.max(0, maxArith - arithC));
  const remW1 = totalWrong - arithW;
  const reasonW = Math.min(remW1, Math.max(0, maxReason - reasonC));
  const genW = remW1 - reasonW;

  const arithTime = Math.round(totalDuration * (maxArith / 200));
  const reasonTime = Math.round(totalDuration * (maxReason / 200));
  const genTime = Math.max(0, totalDuration - arithTime - reasonTime);

  return {
    arithmetic: {
      score: (arithC * 1.0 - arithW * 0.20).toFixed(1),
      maxMarks: maxArith,
      correct: arithC,
      wrong: arithW,
      accuracy: (arithC + arithW) > 0 ? Math.round((arithC / (arithC + arithW)) * 100) : 0,
      time: arithTime,
    },
    reasoning: {
      score: (reasonC * 1.0 - reasonW * 0.20).toFixed(1),
      maxMarks: maxReason,
      correct: reasonC,
      wrong: reasonW,
      accuracy: (reasonC + reasonW) > 0 ? Math.round((reasonC / (reasonC + reasonW)) * 100) : 0,
      time: reasonTime,
    },
    general: {
      score: (genC * 1.0 - genW * 0.20).toFixed(1),
      maxMarks: maxGen,
      correct: genC,
      wrong: genW,
      accuracy: (genC + genW) > 0 ? Math.round((genC / (genC + genW)) * 100) : 0,
      time: genTime,
    },
  };
}

export default function Dashboard() {
  const { user, loading: authLoading } = useAuth();
  const navigate = useNavigate();
  const [searchParams, setSearchParams] = useSearchParams();
  const activeTab = searchParams.get('tab') === 'tests' ? 'tests' : 'dashboard';

  const [attempts, setAttempts] = useState([]);
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [inProgressTests, setInProgressTests] = useState({});
  const [difficultyFilter, setDifficultyFilter] = useState('all');
  const [selectedTestForModal, setSelectedTestForModal] = useState(null);
  const [showCheckoutModal, setShowCheckoutModal] = useState(false);
  const [targetUnlockTest, setTargetUnlockTest] = useState('tsplrb-si-mock-full-200');

  // Read in-progress tests strictly scoped to the active candidate account
  useEffect(() => {
    try {
      if (!user?.email) {
        setInProgressTests({});
        return;
      }
      const prog = {};
      const currentEmail = String(user.email).toLowerCase().trim();
      ALL_TEST_IDS.forEach((id) => {
        const key = getExamProgressKey(user.email, id);
        const stored = localStorage.getItem(key);
        if (stored) {
          const p = JSON.parse(stored);
          const savedEmail = p.userEmail ? String(p.userEmail).toLowerCase().trim() : null;
          if (savedEmail === currentEmail && p.answers && Object.keys(p.answers).length > 0) {
            prog[id] = p;
          }
        }
      });
      setInProgressTests(prog);
    } catch (e) {
      console.warn('Error reading user exam progress:', e);
    }
  }, [user?.email]);

  useEffect(() => {
    async function loadAttempts() {
      if (!user?.email) {
        setLoading(false);
        return;
      }
      try {
        const res = await fetch('/api/attempts', {
          headers: { 'x-user-email': user.email },
        });
        const data = await res.json();
        setAttempts(data.attempts || []);
        setStats(data.stats || null);
      } catch (err) {
        console.error('Failed to load past attempts:', err);
      } finally {
        setLoading(false);
      }
    }

    if (user) {
      loadAttempts();
    } else if (!authLoading) {
      setLoading(false);
    }
  }, [user, authLoading]);

  const isAdmin = user?.role === 'admin' && user?.email?.toLowerCase().trim() === 'varshithpoudala@gmail.com';
  const isPaid = user?.isPaid || isAdmin;

  const handleTabChange = (tab) => {
    if (tab === 'tests') {
      setSearchParams({ tab: 'tests' });
    } else {
      setSearchParams({});
    }
  };

  if (authLoading) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center">
        <div className="w-8 h-8 border-3 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-4">
        <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-8 text-center shadow-lg">
          <div className="w-12 h-12 bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-amber-400 rounded-xl flex items-center justify-center mx-auto mb-4 border border-slate-200 dark:border-slate-700">
            <Trophy className="w-6 h-6" />
          </div>
          <h1 className="text-xl font-bold text-slate-900 dark:text-white mb-2">Sign In to View Dashboard</h1>
          <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
            Track your scores, re-take mock tests multiple times, and view in-depth performance analytics.
          </p>
          <Link
            to="/login"
            className="inline-block w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl transition-colors text-xs shadow-xs"
          >
            Sign In to Continue
          </Link>
        </div>
      </div>
    );
  }

  const inProgressKeys = Object.keys(inProgressTests);

  const testCatalog = [
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
      testId: 'tsplrb-si-mock-full-200-6',
      title: 'TSPLRB SI Mock Test 6 (Speed & Accuracy Practice PWT)',
      difficulty: 'Medium',
      badge: 'MEDIUM • SPEED & ACCURACY',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'High-yield 200Q speed-building mock. Calibrated for optimal time allocation across Arithmetic, Reasoning, and General Studies with 2026 Current Affairs.',
    },
    {
      testId: 'tsplrb-si-mock-full-200-5',
      title: 'TSPLRB SI Mock Test 5 (Hard • Advanced High-Yield PWT)',
      difficulty: 'Hard',
      badge: 'HARD • ADVANCED SIMULATION',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'High-difficulty 200Q simulation modeling recent TSPSC and TSPLRB trends. Advanced statement-based questions and intricate puzzles.',
    },
    {
      testId: 'tsplrb-si-mock-full-200-7',
      title: 'TSPLRB SI Mock Test 7 (Grand Master Championship Simulation)',
      difficulty: 'Hard',
      badge: 'HARD • CHAMPIONSHIP TIER',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'Championship-tier 200Q simulation featuring multi-statement analytical GS, higher-order reasoning puzzles, and advanced arithmetic.',
    },
    {
      testId: 'tsplrb-si-mock-full-200-8',
      title: 'TSPLRB SI Mock Test 8 (Medium • Official Standard PWT)',
      difficulty: 'Medium',
      badge: 'MEDIUM • 2022 PWT BLUEPRINT',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'Official 200Q Standard Blueprint: 50 Arithmetic + 50 Reasoning + 100 General Studies & Telangana Movement.',
    },
    {
      testId: 'tsplrb-si-mock-full-200-9',
      title: 'TSPLRB SI Mock Test 9 (Advanced Practice & 2026 High-Yield PWT)',
      difficulty: 'Hard',
      badge: 'HARD • ADVANCED 2026 PWT',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'Advanced Practice Paper integrating latest 2026 faculty questions, Telangana policies (HYDRAA, Bhoo Bharati, Caste Survey, Musi Project), and comprehensive Arithmetic & Reasoning.',
    },
    {
      testId: 'tsplrb-si-mock-full-200-10',
      title: 'TSPLRB SI Mock Test 10 (Master Model Paper • Latest Civils & PWT Standard)',
      difficulty: 'Medium',
      badge: 'NEW • 2026 CIVIL SERVICES & PWT STANDARD',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'Master 200Q model paper calibrated on Civils/TSPSC standards: Speed-Distance-Time, Mensuration 2D/3D, PYQ Calendar Repetition, balanced GS weightage, international summits (BRICS/SCO/G20), and 2026 governance reforms.',
    },
    {
      testId: 'tsplrb-si-mock-full-200-11',
      title: 'TSPLRB SI Mock Test 11 (High-Yield 2026 Reserve Bank • Final PWT Benchmark)',
      difficulty: 'Hard',
      badge: 'NEW • 2026 RESERVE BANK & FINAL PWT BENCHMARK',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'Comprehensive 200Q benchmark paper assembled from verified reserve faculty pools: Speed-Distance-Time, Mensuration 2D/3D, Calendar Repetition, Telangana Armed Struggle & Statehood, Indian Polity, National Movement, and 2026 Current Affairs.',
    },
    {
      testId: 'tsplrb-si-mock-full-200-12',
      title: 'TSPLRB SI Mock Test 12 (Easy • Foundational Speed & High-Accuracy PWT)',
      difficulty: 'Easy',
      badge: 'EASY • FOUNDATIONAL SPEED & ACCURACY',
      questions: 200,
      duration: '180 Mins (3 Hrs)',
      marks: 200,
      isFree: false,
      description: 'High-yield foundational 200Q paper designed for rapid solving, formula mastery, and concept reinforcement: Direct Arithmetic, Essential Reasoning, Core Polity Articles, Telangana Heritage & Statehood, and Vital Science.',
    },
  ];

  const filteredTests = testCatalog.filter(
    t => difficultyFilter === 'all' || t.difficulty.toLowerCase() === difficultyFilter.toLowerCase()
  );

  return (
    <main className="flex-1 max-w-[1440px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
      
      {/* 1. TOP CANDIDATE HERO BANNER */}
      <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xs">
        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-5">
          
          {/* Candidate Identity with Crown & Full Access Hover */}
          <div className="flex items-start gap-4">
            <div className="relative group">
              <div className="w-12 h-12 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-black text-lg flex items-center justify-center flex-shrink-0 shadow-xs relative">
                {(user.name || user.email || 'U').charAt(0).toUpperCase()}
                {isPaid && (
                  <div 
                    title="Full Access Active"
                    className="absolute -top-1.5 -right-1.5 bg-amber-500 text-slate-950 p-1 rounded-full shadow-md border-2 border-white dark:border-slate-900 flex items-center justify-center"
                  >
                    <Crown className="w-3 h-3 fill-current" />
                  </div>
                )}
              </div>
              {isPaid && (
                <div className="absolute left-1/2 -translate-x-1/2 -bottom-8 hidden group-hover:flex items-center gap-1 bg-slate-900 dark:bg-slate-800 text-amber-400 text-[10px] font-bold px-2 py-1 rounded shadow-lg whitespace-nowrap z-30 border border-slate-700 pointer-events-none">
                  <Crown className="w-3 h-3 fill-current" />
                  <span>Full Access Active</span>
                </div>
              )}
            </div>

            <div>
              <div className="flex flex-wrap items-center gap-2 mb-1">
                <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">Candidate Dashboard</span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
                  TSPLRB SI 2026 PWT
                </span>
                {isAdmin && (
                  <Link
                    to="/admin"
                    className="inline-flex items-center gap-1 text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-purple-50 dark:bg-purple-950/80 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800 hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors shadow-xs"
                    title="Access Administrator Control Panel"
                  >
                    <Shield className="w-2.5 h-2.5 text-purple-600 dark:text-purple-400" />
                    <span>Super Admin • Admin Panel →</span>
                  </Link>
                )}
              </div>
              <h1 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
                {user.name || user.email}
              </h1>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Preliminary Written Test (PWT) Preparation Hub • 200 Questions • 3 Hours • Bilingual (EN / తెలుగు)
              </p>
            </div>
          </div>

          {/* PERFORMANCE METRICS IN HERO HEADER (Replaces Exam Mode, Cut-off, Negative Marking) */}
          <div className="flex flex-wrap items-center gap-3 w-full lg:w-auto justify-between lg:justify-end">
            <div className="flex items-center gap-2 sm:gap-4 text-xs bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl px-2 sm:px-4 py-2 sm:py-2.5 w-full sm:w-auto justify-between sm:justify-start">
              <div className="text-center px-1 sm:px-2 flex-1 sm:flex-initial">
                <div className="text-[10px] text-slate-400 font-semibold uppercase">Attempts</div>
                <div className="font-extrabold text-slate-900 dark:text-white text-sm sm:text-base">
                  {stats?.totalAttempts || 0}
                </div>
              </div>
              <div className="w-px h-6 bg-slate-200 dark:border-slate-800" />
              <div className="text-center px-1 sm:px-2 flex-1 sm:flex-initial">
                <div className="text-[10px] text-slate-400 font-semibold uppercase">Best Score</div>
                <div className="font-extrabold text-slate-900 dark:text-white text-sm sm:text-base whitespace-nowrap">
                  {stats?.bestScore || 0} <span className="text-[10px] font-normal text-slate-400">/ 200</span>
                </div>
              </div>
              <div className="w-px h-6 bg-slate-200 dark:border-slate-800" />
              <div className="text-center px-1 sm:px-2 flex-1 sm:flex-initial">
                <div className="text-[10px] text-slate-400 font-semibold uppercase">Avg Score</div>
                <div className="font-extrabold text-slate-900 dark:text-white text-sm sm:text-base">
                  {stats?.averageScore || 0}
                </div>
              </div>
              <div className="w-px h-6 bg-slate-200 dark:border-slate-800" />
              <div className="text-center px-1 sm:px-2 flex-1 sm:flex-initial">
                <div className="text-[10px] text-slate-400 font-semibold uppercase">Accuracy</div>
                <div className="font-extrabold text-emerald-600 dark:text-emerald-400 text-sm sm:text-base">
                  {stats?.averageAccuracy || 0}%
                </div>
              </div>
            </div>

            {!isPaid && (
              <button
                onClick={() => {
                  setTargetUnlockTest('tsplrb-si-mock-full-200');
                  setShowCheckoutModal(true);
                }}
                className="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-3.5 py-2 rounded-xl transition-colors shadow-xs flex items-center gap-1.5 cursor-pointer"
              >
                <Lock className="w-3.5 h-3.5" />
                <span>Unlock All ₹99</span>
              </button>
            )}
          </div>

        </div>

        {/* In-page Tab Switcher */}
        <div className="mt-5 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2 bg-slate-100 dark:bg-slate-950 p-1 rounded-xl border border-slate-200 dark:border-slate-800 text-xs font-bold">
            <button
              onClick={() => handleTabChange('dashboard')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all cursor-pointer ${
                activeTab === 'dashboard'
                  ? 'bg-white dark:bg-slate-800 text-blue-600 dark:text-blue-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <LayoutDashboard className="w-3.5 h-3.5" />
              <span>Dashboard & Analytics</span>
            </button>
            <button
              onClick={() => handleTabChange('tests')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all cursor-pointer ${
                activeTab === 'tests'
                  ? 'bg-white dark:bg-slate-800 text-blue-600 dark:text-blue-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Mock Tests ({testCatalog.length} Papers)</span>
            </button>
          </div>

          <div className="hidden sm:flex items-center text-xs text-slate-500 dark:text-slate-400">
            {activeTab === 'dashboard' ? (
              <span>Viewing candidate performance history & diagnostic stats</span>
            ) : (
              <span>Viewing {testCatalog.length} official full-length simulated CBT papers</span>
            )}
          </div>
        </div>

      </div>

      {/* ============================================================== */}
      {/* TAB 1: DASHBOARD TAB (NO TESTS SHOWN - PURE PERFORMANCE & STATS) */}
      {/* ============================================================== */}
      {activeTab === 'dashboard' && (
        <div className="mt-6 space-y-6">
          
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
                    {testCatalog.find(t => t.testId === inProgressKeys[0])?.title || inProgressKeys[0]} • {Object.keys(inProgressTests[inProgressKeys[0]]?.answers || {}).length} questions answered
                  </div>
                </div>
              </div>

              <Link
                to={`/exam/${inProgressKeys[0]}`}
                className="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs px-4 py-2 rounded-xl transition-colors shadow-xs flex items-center gap-1.5 flex-shrink-0"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Resume Test Now</span>
              </Link>
            </div>
          )}

          {/* 2-COLUMN LAYOUT: MAIN RESULTS TABLE (8 cols) + EXAM STATS & STRATEGY (4 cols) */}
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 w-full min-w-0">
            
            {/* LEFT: Previous Results & Attempt History Table with Category Hover Cards */}
            <div className="lg:col-span-8 space-y-6 min-w-0">
              
              <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-xs min-w-0">
                <div className="p-4 sm:p-5 border-b border-slate-100 dark:border-slate-800 flex items-center justify-between">
                  <div>
                    <h2 className="text-sm sm:text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                      <FileText className="w-4 h-4 text-blue-600 dark:text-amber-400" />
                      Previous Results & Attempt History
                    </h2>
                    <p className="text-xs text-slate-500 dark:text-slate-400">
                      Hover over Score, Accuracy, and Correct/Wrong to view category-wise breakdowns
                    </p>
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

                      <button
                        onClick={() => handleTabChange('tests')}
                        className="inline-flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs px-4 py-2 rounded-xl transition-colors shadow-xs cursor-pointer"
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                        <span>Go to Mock Tests Tab</span>
                      </button>
                    </div>
                  </div>
                ) : (
                  <div className="overflow-x-auto pb-16 w-full max-w-full">
                    <table className="w-full text-left text-xs text-slate-700 dark:text-slate-300">
                      <thead className="bg-slate-50 dark:bg-slate-950/60 text-slate-500 dark:text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-200 dark:border-slate-800">
                        <tr>
                          <th className="py-3 px-4">Test Name</th>
                          <th className="py-3 px-4">Attempt</th>
                          <th className="py-3 px-4">Date</th>
                          <th className="py-3 px-4">Score</th>
                          <th className="py-3 px-4">Accuracy</th>
                          <th className="py-3 px-4">Correct / Wrong</th>
                          <th className="py-3 px-4">Time Taken</th>
                          <th className="py-3 px-4 text-right">Actions</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-100 dark:divide-slate-800">
                        {attempts.map((att, idx) => {
                          const testLabel = att.testId?.includes('demo') ? '50-Q Free Demo Mock' : 'Full 200-Q Mock Test';
                          const metrics = getAttemptCategoryMetrics(att);
                          const openDown = idx < 2; // Rows 0 and 1 open downward to avoid clipping by table header

                          const scoreItems = [
                            { label: 'Arithmetic', value: `${metrics.arithmetic.score} / ${metrics.arithmetic.maxMarks} M`, color: 'text-blue-400' },
                            { label: 'Reasoning', value: `${metrics.reasoning.score} / ${metrics.reasoning.maxMarks} M`, color: 'text-purple-400' },
                            { label: 'GS & Telangana', value: `${metrics.general.score} / ${metrics.general.maxMarks} M`, color: 'text-emerald-400' },
                          ];

                          const accuracyItems = [
                            { label: 'Arithmetic', value: `${metrics.arithmetic.accuracy}%`, color: 'text-blue-400' },
                            { label: 'Reasoning', value: `${metrics.reasoning.accuracy}%`, color: 'text-purple-400' },
                            { label: 'GS & Telangana', value: `${metrics.general.accuracy}%`, color: 'text-emerald-400' },
                          ];

                          const breakdownItems = [
                            { label: 'Arithmetic', value: `${metrics.arithmetic.correct}✓ / ${metrics.arithmetic.wrong}✗`, color: 'text-blue-400' },
                            { label: 'Reasoning', value: `${metrics.reasoning.correct}✓ / ${metrics.reasoning.wrong}✗`, color: 'text-purple-400' },
                            { label: 'GS & Telangana', value: `${metrics.general.correct}✓ / ${metrics.general.wrong}✗`, color: 'text-emerald-400' },
                          ];

                          const timeItems = [
                            { label: 'Arithmetic', value: formatDuration(metrics.arithmetic.time), color: 'text-blue-400' },
                            { label: 'Reasoning', value: formatDuration(metrics.reasoning.time), color: 'text-purple-400' },
                            { label: 'GS & Telangana', value: formatDuration(metrics.general.time), color: 'text-emerald-400' },
                          ];

                          return (
                            <tr key={att.id} className="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors">
                              <td className="py-3.5 px-4 font-semibold text-slate-900 dark:text-white">
                                {testLabel}
                              </td>
                              <td className="py-3.5 px-4">
                                <span className="whitespace-nowrap inline-flex items-center px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                                  Attempt #{att.attemptNumber || 1}
                                </span>
                              </td>
                              <td className="py-3.5 px-4 text-slate-500 dark:text-slate-400 whitespace-nowrap">
                                {new Date(att.submittedAt).toLocaleDateString('en-IN', {
                                  day: 'numeric',
                                  month: 'short',
                                  year: 'numeric',
                                })}
                              </td>

                              {/* Hover on Score: Category-wise Marks */}
                              <td className="py-3.5 px-4 relative group cursor-pointer whitespace-nowrap">
                                <span className="font-bold text-slate-900 dark:text-amber-400 text-sm border-b border-dotted border-amber-500 pb-0.5">
                                  {att.totalScore} <span className="text-[10px] text-slate-400 font-normal">/ {att.totalMarks}</span>
                                </span>
                                <CategoryHoverCard title="Score Breakdown" items={scoreItems} openDown={openDown} />
                              </td>

                              {/* Hover on Accuracy: Category-wise Accuracy */}
                              <td className="py-3.5 px-4 relative group cursor-pointer whitespace-nowrap">
                                <span className="font-semibold text-emerald-600 dark:text-emerald-400 border-b border-dotted border-emerald-500 pb-0.5">
                                  {att.accuracyPercent}%
                                </span>
                                <CategoryHoverCard title="Accuracy Breakdown" items={accuracyItems} openDown={openDown} />
                              </td>

                              {/* Hover on Correct / Wrong: Category-wise Correct/Wrong */}
                              <td className="py-3.5 px-4 relative group cursor-pointer whitespace-nowrap">
                                <div className="inline-block border-b border-dotted border-slate-400 pb-0.5">
                                  <span className="text-emerald-600 dark:text-emerald-400 font-bold">{att.correctCount} ✓</span>
                                  <span className="text-slate-400 mx-1">/</span>
                                  <span className="text-rose-600 dark:text-rose-400 font-bold">{att.wrongCount} ✗</span>
                                </div>
                                <CategoryHoverCard title="Correct / Wrong" items={breakdownItems} openDown={openDown} />
                              </td>

                              {/* Hover on Time Taken: Category-wise Time */}
                              <td className="py-3.5 px-4 relative group cursor-pointer whitespace-nowrap">
                                <span className="font-semibold text-slate-800 dark:text-slate-200 border-b border-dotted border-blue-400 pb-0.5">
                                  ⏱ {formatDuration(att.durationSeconds)}
                                </span>
                                <CategoryHoverCard title="Time Breakdown" items={timeItems} openDown={openDown} />
                              </td>

                              <td className="py-3.5 px-4 text-right">
                                <button
                                  onClick={() => {
                                    const targetTest = testCatalog.find(t => t.testId === att.testId) || {
                                      testId: att.testId,
                                      title: att.testId?.includes('demo') ? 'TSPLRB SI Free Demo Mock Test' : 'TSPLRB SI Mock Test',
                                      questions: att.totalMarks || 200,
                                      duration: att.totalMarks === 50 ? '45 Mins' : '180 Mins (3 Hrs)',
                                      marks: att.totalMarks || 200,
                                      difficulty: 'Medium',
                                      badge: 'MOCK TEST',
                                    };
                                    setSelectedTestForModal(targetTest);
                                  }}
                                  className="whitespace-nowrap inline-flex items-center gap-1.5 bg-blue-50 hover:bg-blue-100 dark:bg-blue-950/60 dark:hover:bg-blue-900/60 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 px-3 py-1.5 rounded-lg text-xs font-bold transition-all shadow-xs cursor-pointer"
                                >
                                  <span>Retake Test</span>
                                  <ChevronRight className="w-3.5 h-3.5" />
                                </button>
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

            {/* RIGHT SIDEBAR: Exam Pattern & Cut-offs & Strategy */}
            <div className="lg:col-span-4 space-y-6">
              
              {/* Official PWT Exam Pattern & Cut-Offs */}
              <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 shadow-xs">
                <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5 mb-3">
                  <Target className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                  PWT Exam Pattern & Cut-Offs
                </h3>

                <div className="space-y-2.5 text-xs">
                  <div className="flex items-center justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                    <span className="text-slate-500">Total Questions</span>
                    <span className="font-bold text-slate-900 dark:text-white">200 Questions</span>
                  </div>
                  <div className="flex items-center justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                    <span className="text-slate-500">Total Marks</span>
                    <span className="font-bold text-slate-900 dark:text-white">200 Marks</span>
                  </div>
                  <div className="flex items-center justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                    <span className="text-slate-500">Exam Duration</span>
                    <span className="font-bold text-slate-900 dark:text-white">3 Hours (180 mins)</span>
                  </div>
                  <div className="flex items-center justify-between py-1 border-b border-slate-100 dark:border-slate-800">
                    <span className="text-slate-500">Negative Penalty</span>
                    <span className="font-bold text-rose-600 dark:text-rose-400">-0.20 Marks (1/5th)</span>
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800">
                  <div className="text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-2">
                    Official Minimum Qualifying Marks:
                  </div>
                  <div className="grid grid-cols-3 gap-1.5 text-center">
                    <div className="bg-slate-50 dark:bg-slate-950 p-2 rounded-lg border border-slate-200 dark:border-slate-800">
                      <div className="text-[10px] text-slate-400">OC (30%)</div>
                      <div className="font-bold text-xs text-slate-900 dark:text-white">60 Marks</div>
                    </div>
                    <div className="bg-slate-50 dark:bg-slate-950 p-2 rounded-lg border border-slate-200 dark:border-slate-800">
                      <div className="text-[10px] text-slate-400">BC (25%)</div>
                      <div className="font-bold text-xs text-slate-900 dark:text-white">50 Marks</div>
                    </div>
                    <div className="bg-slate-50 dark:bg-slate-950 p-2 rounded-lg border border-slate-200 dark:border-slate-800">
                      <div className="text-[10px] text-slate-400">SC/ST (20%)</div>
                      <div className="font-bold text-xs text-slate-900 dark:text-white">40 Marks</div>
                    </div>
                  </div>
                </div>
              </div>

            </div>

          </div>

          {/* ITEM 5: BOTTOM "TAKE TEST" BANNER BUTTON */}
          <div className="bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white rounded-2xl p-6 sm:p-8 flex flex-col sm:flex-row items-center justify-between gap-6 shadow-xl border border-blue-800/40">
            <div className="text-center sm:text-left">
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-blue-800/80 text-blue-200 text-xs font-bold border border-blue-700 mb-2">
                <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                <span>Ready to Test Your Preparation?</span>
              </div>
              <h2 className="text-xl sm:text-2xl font-black">
                Take a Full-Length TSPLRB SI Mock Test
              </h2>
              <p className="text-xs sm:text-sm text-blue-200/80 mt-1 max-w-xl">
                {isPaid 
                  ? 'All 8 full-length simulated mock tests are unlocked and ready for you with instant scoring and bilingual solutions.'
                  : 'Start with the Free 50-Q Demo Test or unlock all 7 full 200-question papers for just ₹99.'}
              </p>
            </div>

            <button
              onClick={() => handleTabChange('tests')}
              className="bg-white hover:bg-slate-100 text-slate-950 font-black text-sm px-6 py-3.5 rounded-xl transition-all shadow-lg flex items-center gap-2 cursor-pointer flex-shrink-0 hover:scale-105"
            >
              <span>Take Test Now</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>

        </div>
      )}

      {/* ============================================================== */}
      {/* TAB 2: TESTS TAB (CATALOG OF ALL 8 PAPERS WITH LOCK & MODAL) */}
      {/* ============================================================== */}
      {activeTab === 'tests' && (
        <div className="mt-6 space-y-6">
          
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xs">
            <div>
              <h2 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                Available Mock Test Papers ({testCatalog.length} Papers)
              </h2>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                Full 200-Question CBT papers categorized by difficulty: Easy, Medium, and Hard
              </p>
            </div>

            {/* Difficulty Filter Tabs */}
            <div className="flex items-center gap-1 bg-slate-100 dark:bg-slate-950 p-1 rounded-xl border border-slate-200 dark:border-slate-800">
              {[
                { label: 'All', key: 'all', count: testCatalog.length },
                { label: 'Easy', key: 'Easy', count: testCatalog.filter(t => t.difficulty.toLowerCase() === 'easy').length },
                { label: 'Medium', key: 'Medium', count: testCatalog.filter(t => t.difficulty.toLowerCase() === 'medium').length },
                { label: 'Hard', key: 'Hard', count: testCatalog.filter(t => t.difficulty.toLowerCase() === 'hard').length },
              ].map((item) => (
                <button
                  key={item.key}
                  onClick={() => setDifficultyFilter(item.key)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5 ${
                    difficultyFilter === item.key
                      ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs'
                      : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'
                  }`}
                >
                  <span>{item.label}</span>
                  <span className="opacity-70 text-[10px]">({item.count})</span>
                </button>
              ))}
            </div>
          </div>

          {/* Test Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {filteredTests.map((test) => {
              const hasProgress = inProgressTests[test.testId];
              const isUnlocked = test.isFree || isPaid;

              let badgeClasses = 'bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border-blue-200 dark:border-blue-800';
              if (test.difficulty === 'Easy') badgeClasses = 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800';
              else if (test.difficulty === 'Hard') badgeClasses = 'bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 border-rose-200 dark:border-rose-800';

              return (
                <div 
                  key={test.testId} 
                  className={`bg-white dark:bg-slate-900 border rounded-2xl p-5 sm:p-6 transition-all flex flex-col justify-between shadow-xs relative ${
                    isUnlocked 
                      ? 'border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 hover:shadow-md' 
                      : 'border-slate-200 dark:border-slate-800 opacity-90'
                  }`}
                >
                  <div>
                    <div className="flex items-center justify-between mb-2.5">
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

                    <h3 className="font-bold text-slate-900 dark:text-white text-base">{test.title}</h3>
                    <p className="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
                      {test.description}
                    </p>
                  </div>

                  <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                    <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">
                      {hasProgress ? `${Object.keys(hasProgress.answers || {}).length}/${test.questions} Answered` : `${test.marks} Marks`}
                    </span>

                    {hasProgress ? (
                      <Link
                        to={`/exam/${test.testId}`}
                        className="bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold text-xs px-4 py-2 rounded-xl transition-colors shadow-xs flex items-center gap-1.5"
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                        <span>Resume Exam</span>
                      </Link>
                    ) : isUnlocked ? (
                      <button
                        onClick={() => setSelectedTestForModal(test)}
                        className={`font-bold text-xs px-4 py-2 rounded-xl transition-colors shadow-xs flex items-center gap-1.5 cursor-pointer ${
                          test.isFree
                            ? 'bg-blue-600 hover:bg-blue-700 text-white'
                            : 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100'
                        }`}
                      >
                        <span>Start Exam</span>
                        <ChevronRight className="w-3.5 h-3.5" />
                      </button>
                    ) : (
                      <div className="flex items-center gap-2">
                        <span className="text-[10px] text-slate-400 flex items-center gap-1">
                          <Lock className="w-3 h-3" />
                          <span>Locked</span>
                        </span>
                        <button
                          onClick={() => {
                            setTargetUnlockTest(test.testId);
                            setShowCheckoutModal(true);
                          }}
                          className="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs px-3.5 py-1.5 rounded-lg transition-colors flex items-center gap-1 shadow-xs cursor-pointer"
                        >
                          <Lock className="w-3 h-3" />
                          <span>Unlock ₹99</span>
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>

        </div>
      )}

      {/* ============================================================== */}
      {/* ITEM 4: PRE-EXAM INSTRUCTIONS MODAL (SHOWS EXAM SPECS & CUT-OFFS) */}
      {/* ============================================================== */}
      {selectedTestForModal && (
        <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl sm:rounded-3xl p-5 sm:p-8 max-w-xl w-full shadow-2xl relative my-4 sm:my-8 animate-in fade-in zoom-in-95 duration-200">
            
            {/* Close Button */}
            <button
              onClick={() => setSelectedTestForModal(null)}
              className="absolute top-4 right-4 sm:top-5 sm:right-5 p-1.5 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer"
            >
              <X className="w-5 h-5" />
            </button>

            {/* Test Header */}
            <div className="text-left mb-4 sm:mb-5 pr-8">
              <div className="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-0.5 sm:py-1 rounded-full bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 text-xs font-bold border border-blue-200 dark:border-blue-800 mb-2">
                <span>{selectedTestForModal.badge}</span>
                <span>•</span>
                <span>{selectedTestForModal.difficulty}</span>
              </div>
              <h2 className="text-lg sm:text-2xl font-black text-slate-900 dark:text-white leading-tight">
                {selectedTestForModal.title}
              </h2>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                Official TSPLRB SI Preliminary Written Test (PWT) Examination Instructions
              </p>
            </div>

            {/* Key Exam Parameters (Exam Mode, Cut-Offs, Negative Marking) */}
            <div className="grid grid-cols-3 gap-1.5 sm:gap-2.5 bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl sm:rounded-2xl p-2.5 sm:p-4 mb-4 sm:mb-5 text-center">
              <div>
                <div className="text-[9px] sm:text-[10px] text-slate-400 font-semibold uppercase tracking-wider">Exam Mode</div>
                <div className="font-extrabold text-[11px] sm:text-sm text-slate-900 dark:text-white mt-0.5">Online CBT</div>
                <div className="text-[8px] sm:text-[9px] text-slate-400 mt-0.5">Dual EN / తెలుగు</div>
              </div>
              <div className="border-x border-slate-200 dark:border-slate-800">
                <div className="text-[9px] sm:text-[10px] text-slate-400 font-semibold uppercase tracking-wider">Target Cut-Off</div>
                <div className="font-extrabold text-[11px] sm:text-sm text-emerald-600 dark:text-emerald-400 mt-0.5 whitespace-nowrap">
                  {selectedTestForModal.questions === 50 ? '15/50 (OC)' : '60/200 (OC)'}
                </div>
                <div className="text-[8px] sm:text-[9px] text-slate-400 mt-0.5 whitespace-nowrap">BC: 50 | SC/ST: 40</div>
              </div>
              <div>
                <div className="text-[9px] sm:text-[10px] text-slate-400 font-semibold uppercase tracking-wider">Negative Marking</div>
                <div className="font-extrabold text-[11px] sm:text-sm text-rose-600 dark:text-rose-400 mt-0.5 whitespace-nowrap">-0.20 Marks</div>
                <div className="text-[8px] sm:text-[9px] text-slate-400 mt-0.5">1/5th deduction</div>
              </div>
            </div>

            {/* Test Specifications Overview */}
            <div className="grid grid-cols-3 gap-2 text-xs mb-5 border-y border-slate-100 dark:border-slate-800 py-3 text-slate-700 dark:text-slate-300">
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-blue-600 flex-shrink-0" />
                <span><strong>{selectedTestForModal.questions}</strong> Questions</span>
              </div>
              <div className="flex items-center gap-1.5">
                <Clock className="w-3.5 h-3.5 text-blue-600 flex-shrink-0" />
                <span><strong>{selectedTestForModal.duration}</strong></span>
              </div>
              <div className="flex items-center gap-1.5">
                <Award className="w-3.5 h-3.5 text-blue-600 flex-shrink-0" />
                <span><strong>{selectedTestForModal.marks}</strong> Marks</span>
              </div>
            </div>

            {/* Instructions List */}
            <div className="text-left bg-slate-50 dark:bg-slate-950/60 rounded-xl p-4 mb-6 border border-slate-100 dark:border-slate-800/80">
              <div className="text-xs font-bold text-slate-900 dark:text-white mb-2 flex items-center gap-1.5">
                <Shield className="w-3.5 h-3.5 text-amber-500" />
                <span>Important CBT Examination Guidelines:</span>
              </div>
              <ul className="space-y-1.5 text-[11px] text-slate-600 dark:text-slate-400">
                <li className="flex items-start gap-1.5">
                  <span className="text-blue-600 font-bold">•</span>
                  <span><strong>+1.0 mark</strong> is awarded for each correct answer.</span>
                </li>
                <li className="flex items-start gap-1.5">
                  <span className="text-rose-600 font-bold">•</span>
                  <span><strong>-0.20 mark</strong> is deducted for each wrong answer (1/5th penalty). No penalty for unattempted questions.</span>
                </li>
                <li className="flex items-start gap-1.5">
                  <span className="text-blue-600 font-bold">•</span>
                  <span>Questions are arranged by sections: Arithmetic, Reasoning & Mental Ability, and General Studies & Telangana.</span>
                </li>
                <li className="flex items-start gap-1.5">
                  <span className="text-blue-600 font-bold">•</span>
                  <span>The timer will start automatically as soon as you click <strong>Continue to Exam</strong>.</span>
                </li>
              </ul>
            </div>

            {/* Action Buttons */}
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={() => setSelectedTestForModal(null)}
                className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 font-semibold text-xs py-3 rounded-xl transition-colors cursor-pointer"
              >
                Cancel
              </button>
              <button
                onClick={() => {
                  const targetId = selectedTestForModal.testId;
                  setSelectedTestForModal(null);
                  navigate(`/exam/${targetId}`);
                }}
                className="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-3 rounded-xl transition-all shadow-md flex items-center justify-center gap-1.5 cursor-pointer hover:scale-[1.02]"
              >
                <span>Continue to Exam</span>
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>

          </div>
        </div>
      )}

      {/* Checkout Modal */}
      <CheckoutModal
        isOpen={showCheckoutModal}
        onClose={() => setShowCheckoutModal(false)}
        targetTestId={targetUnlockTest}
        onSuccess={() => {
          setShowCheckoutModal(false);
          navigate(`/exam/${targetUnlockTest || 'tsplrb-si-mock-full-200'}`);
        }}
      />

    </main>
  );
}
