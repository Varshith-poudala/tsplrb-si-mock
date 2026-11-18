import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { 
  Clock, Shield, Globe, Menu, X, CheckCircle2, Bookmark, ArrowLeft, ArrowRight, 
  RotateCcw, AlertTriangle, Trophy, Award, Lock, BookOpen, ChevronLeft, ChevronRight,
  Layers, Check, Pause, Play, Save, AlertCircle, HelpCircle, LayoutGrid, Sun, Moon
} from 'lucide-react';
import confetti from 'canvas-confetti';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { getExamProgressKey } from '../utils/storage';
import CheckoutModal from '../components/CheckoutModal';

const QUESTIONS_PER_PAGE = 10;

export default function Exam() {
  const { id: testId = 'demo-test-50' } = useParams();
  const navigate = useNavigate();
  const { user } = useAuth();
  const { theme, toggleTheme } = useTheme();

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [testMeta, setTestMeta] = useState(null);
  const [questions, setQuestions] = useState([]);

  // Pagination State (10 Questions Per Page)
  const [currentPage, setCurrentPage] = useState(1);
  const [highlightedQ, setHighlightedQ] = useState(null);

  // Exam Progress State
  const [answers, setAnswers] = useState({});
  const [markedForReview, setMarkedForReview] = useState(new Set());
  const [visited, setVisited] = useState(new Set());

  // Palette & Language
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [paletteSectionFilter, setPaletteSectionFilter] = useState('all');
  const [langMode, setLangMode] = useState('dual');
  const [timeLeft, setTimeLeft] = useState(180 * 60);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Time metrics per category (Item 9)
  const [categoryTime, setCategoryTime] = useState({
    arithmetic: 0,
    reasoning: 0,
    general: 0,
  });
  const activeCategoryRef = useRef('arithmetic');

  // Pause & Exit Modal States
  const [isPaused, setIsPaused] = useState(false);
  const [showExitModal, setShowExitModal] = useState(false);
  const [resumePrompt, setResumePrompt] = useState(null);
  const [showCheckoutModal, setShowCheckoutModal] = useState(false);

  // Result / Review State
  const [showResultModal, setShowResultModal] = useState(false);
  const [resultData, setResultData] = useState(null);
  const [reviewMode, setReviewMode] = useState(false);

  // Timer Ref
  const timerRef = useRef(null);
  const startTimeRef = useRef(Date.now());

  // Persist progress helper (strictly scoped to authenticated user)
  const saveProgressToStorage = useCallback((customAnswers, customMarked, customVisited, customTimeLeft, customPage, customCategoryTime) => {
    try {
      const cleanUserEmail = user?.email ? String(user.email).toLowerCase().trim() : null;
      const storageKey = getExamProgressKey(user?.email, testId);
      const payload = {
        testId,
        userEmail: cleanUserEmail,
        answers: customAnswers || answers,
        markedForReview: Array.from(customMarked || markedForReview),
        visited: Array.from(customVisited || visited),
        timeLeft: customTimeLeft !== undefined ? customTimeLeft : timeLeft,
        currentPage: customPage || currentPage,
        categoryTime: customCategoryTime || categoryTime,
        savedAt: new Date().toISOString(),
      };
      localStorage.setItem(storageKey, JSON.stringify(payload));
      // Remove any legacy unscoped key to prevent cross-account leaks
      localStorage.removeItem(`exam_progress_${testId}`);
    } catch (e) {
      console.warn('Could not save exam progress to storage:', e);
    }
  }, [testId, user?.email, answers, markedForReview, visited, timeLeft, currentPage, categoryTime]);

  const clearSavedProgress = useCallback(() => {
    try {
      const storageKey = getExamProgressKey(user?.email, testId);
      localStorage.removeItem(storageKey);
      localStorage.removeItem(`exam_progress_${testId}`);
    } catch (e) {}
  }, [testId, user?.email]);

  // Fetch Questions
  useEffect(() => {
    async function fetchQuestions() {
      setLoading(true);
      setError(null);
      try {
        const headers = {};
        if (user?.email) headers['x-user-email'] = user.email;

        const res = await fetch(`/api/tests/${testId}/questions`, { headers });
        const data = await res.json();

        if (res.status === 402) {
          setError({ isLocked: true, message: data.message });
          setLoading(false);
          return;
        }

        if (!res.ok) {
          throw new Error(data.error || 'Failed to load test questions');
        }

        setTestMeta({
          testId: data.testId,
          totalQuestions: data.totalQuestions,
          durationMinutes: data.durationMinutes,
          marksPerQuestion: data.marksPerQuestion,
          negativeMarking: data.negativeMarking,
        });
        setQuestions(data.questions || []);

        // Initialize timer
        const initialSeconds = (data.durationMinutes || 180) * 60;
        setTimeLeft(initialSeconds);

        // Check for saved progress in localStorage (scoped to current user)
        const storageKey = getExamProgressKey(user?.email, testId);
        const stored = localStorage.getItem(storageKey);
        if (stored) {
          try {
            const parsed = JSON.parse(stored);
            const currentEmail = user?.email ? String(user.email).toLowerCase().trim() : null;
            const savedEmail = parsed.userEmail ? String(parsed.userEmail).toLowerCase().trim() : null;
            // Only resume if progress explicitly matches current user
            if ((!currentEmail && !savedEmail) || (currentEmail && savedEmail === currentEmail)) {
              if (parsed.answers && Object.keys(parsed.answers).length > 0) {
                setResumePrompt(parsed);
              }
            }
          } catch (e) {}
        }
      } catch (err) {
        setError({ message: err.message });
      } finally {
        setLoading(false);
      }
    }

    fetchQuestions();
  }, [testId, user]);

  const totalQuestions = questions.length || (testMeta?.totalQuestions || 200);
  const totalPages = Math.ceil(totalQuestions / QUESTIONS_PER_PAGE) || 1;

  // Active page question slice
  const startIndex = (currentPage - 1) * QUESTIONS_PER_PAGE;
  const currentQuestions = questions.slice(startIndex, startIndex + QUESTIONS_PER_PAGE);

  // Section Ranges & Dynamic Section Detection
  const isDemo = totalQuestions <= 50;
  const sectionRanges = isDemo ? [
    { key: 'arithmetic', name: 'Arithmetic & Number Ability', shortName: 'Arithmetic', startQ: 1, endQ: 15, total: 15 },
    { key: 'reasoning', name: 'Reasoning & Mental Ability', shortName: 'Reasoning', startQ: 16, endQ: 30, total: 15 },
    { key: 'general', name: 'General Studies & Telangana', shortName: 'GS & Telangana', startQ: 31, endQ: 50, total: 20 },
  ] : [
    { key: 'arithmetic', name: 'Arithmetic & Number Ability', shortName: 'Arithmetic', startQ: 1, endQ: 50, total: 50 },
    { key: 'reasoning', name: 'Reasoning & Mental Ability', shortName: 'Reasoning', startQ: 51, endQ: 100, total: 50 },
    { key: 'general', name: 'General Studies & Telangana', shortName: 'GS & Telangana', startQ: 101, endQ: 200, total: 100 },
  ];

  const firstQOnPage = startIndex + 1;
  const currentSection = sectionRanges.find(s => firstQOnPage >= s.startQ && firstQOnPage <= s.endQ) || sectionRanges[0];

  useEffect(() => {
    if (currentSection) {
      activeCategoryRef.current = currentSection.key;
    }
  }, [currentSection]);

  // Timer Tick & Category-Wise Time Tracking (Item 9)
  useEffect(() => {
    if (loading || isPaused || reviewMode || showResultModal || showExitModal || resumePrompt) {
      clearInterval(timerRef.current);
      return;
    }

    timerRef.current = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timerRef.current);
          handleAutoSubmit();
          return 0;
        }
        return prev - 1;
      });

      setCategoryTime(prev => {
        const catKey = activeCategoryRef.current || 'arithmetic';
        return {
          ...prev,
          [catKey]: (prev[catKey] || 0) + 1,
        };
      });
    }, 1000);

    return () => clearInterval(timerRef.current);
  }, [loading, isPaused, reviewMode, showResultModal, showExitModal, resumePrompt]);

  // Format Timer mm:ss or hh:mm:ss
  const formatTime = (secs) => {
    const hours = Math.floor(secs / 3600);
    const minutes = Math.floor((secs % 3600) / 60);
    const seconds = secs % 60;
    if (hours > 0) {
      return `${hours}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  };

  // Helper to format statements, match the following, and lists with clean line breaks
  const formatQuestionText = (text) => {
    if (!text || typeof text !== 'string') return '';
    // Strip bracket tags like [Advanced Calculation], [Analytical], [క్లిష్టమైన సమస్య], etc. if present
    let clean = text.replace(/^\s*\[(Advanced Calculation|Analytical|Multi-Step Puzzle|క్లిష్టమైన సమస్య|విశ్లేషణాత్మక|బహుళ-దశల పజిల్)\]\s*/i, '');
    
    // Format statements and match the following if they are clumped without newlines
    clean = clean
      .replace(/([^\n])\s*(Statements?:)\s*/gi, '$1\n\n$2\n')
      .replace(/([^\n])\s*(Conclusions?:)\s*/gi, '$1\n\n$2\n')
      .replace(/([^\n])\s*(Arguments?:)\s*/gi, '$1\n\n$2\n')
      .replace(/([^\n])\s*(Assumptions?:)\s*/gi, '$1\n\n$2\n')
      .replace(/([^\n])\s*(Statement\s+[I|V|X|\d]+:?)\s*/gi, '$1\n$2 ')
      .replace(/([^\n])\s*(Conclusion\s+[I|V|X|\d]+:?)\s*/gi, '$1\n$2 ')
      .replace(/([^\n])\s*(Argument\s+[I|V|X|\d]+:?)\s*/gi, '$1\n$2 ')
      .replace(/([^\n])\s*(Assumption\s+[I|V|X|\d]+:?)\s*/gi, '$1\n$2 ')
      .replace(/([^\n])\s*(\([1-4]\)|\b[1-4]\.\s+)(?=[A-Z\u0C00-\u0C7F])/g, '$1\n$2')
      .replace(/([^\n])\s*(List\s*[-–]\s*[I|1]:?)/gi, '$1\n\n$2')
      .replace(/([^\n])\s*(List\s*[-–]\s*[II|2]:?)/gi, '$1\n\n$2')
      .replace(/([^\n])\s*(Match\s+List[-–\s])/gi, '$1\n\n$2')
      .replace(/([^\n])\s*(Which of the following|Which of the statements|Select the correct answer|పై వాటిలో)/gi, '$1\n\n$2')
      .trim();
      
    return clean;
  };

  // Question handlers
  const handleSelectOption = (qNum, optIndex) => {
    if (reviewMode) return;
    const updatedAnswers = { ...answers, [qNum]: optIndex };
    const updatedVisited = new Set(visited).add(qNum);
    setAnswers(updatedAnswers);
    setVisited(updatedVisited);
    saveProgressToStorage(updatedAnswers, null, updatedVisited, null, null);
  };

  const handleClearAnswer = (qNum) => {
    if (reviewMode) return;
    const updatedAnswers = { ...answers };
    delete updatedAnswers[qNum];
    setAnswers(updatedAnswers);
    saveProgressToStorage(updatedAnswers, null, null, null, null);
  };

  const handleToggleReview = (qNum) => {
    if (reviewMode) return;
    const updatedMarked = new Set(markedForReview);
    if (updatedMarked.has(qNum)) updatedMarked.delete(qNum);
    else updatedMarked.add(qNum);
    setMarkedForReview(updatedMarked);
    saveProgressToStorage(null, updatedMarked, null, null, null);
  };

  const handleGoToPage = (pageNum) => {
    if (pageNum < 1 || pageNum > totalPages) return;
    setCurrentPage(pageNum);
    saveProgressToStorage(null, null, null, null, pageNum);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleJumpToQuestion = (qNum) => {
    const targetPage = Math.floor((qNum - 1) / QUESTIONS_PER_PAGE) + 1;
    setCurrentPage(targetPage);
    const updatedVisited = new Set(visited).add(qNum);
    setVisited(updatedVisited);
    saveProgressToStorage(null, null, updatedVisited, null, targetPage);
    setPaletteOpen(false);

    setTimeout(() => {
      const el = document.getElementById(`question-card-${qNum}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        setHighlightedQ(qNum);
        setTimeout(() => setHighlightedQ(null), 2500);
      }
    }, 150);
  };

  const handlePauseTest = () => {
    clearInterval(timerRef.current);
    setIsPaused(true);
    setPaletteOpen(false);
    saveProgressToStorage();
  };

  const handleResumeTest = () => {
    setIsPaused(false);
    setShowExitModal(false);
  };

  const handleAttemptExit = () => {
    if (reviewMode || showResultModal) {
      navigate('/dashboard');
      return;
    }
    clearInterval(timerRef.current);
    setIsPaused(true);
    setPaletteOpen(false);
    saveProgressToStorage();
    setShowExitModal(true);
  };

  const handleConfirmExit = () => {
    saveProgressToStorage();
    setShowExitModal(false);
    navigate('/dashboard');
  };

  const handleDiscardAndQuit = () => {
    clearSavedProgress();
    setShowExitModal(false);
    navigate('/dashboard');
  };

  const handleAcceptResume = () => {
    if (resumePrompt) {
      setAnswers(resumePrompt.answers || {});
      setMarkedForReview(new Set(resumePrompt.markedForReview || []));
      setVisited(new Set(resumePrompt.visited || [1]));
      if (resumePrompt.timeLeft) setTimeLeft(resumePrompt.timeLeft);
      if (resumePrompt.currentPage) setCurrentPage(resumePrompt.currentPage);
      if (resumePrompt.categoryTime) setCategoryTime(resumePrompt.categoryTime);
      setResumePrompt(null);
      setIsPaused(false);
    }
  };

  const handleDeclineResume = () => {
    clearSavedProgress();
    setResumePrompt(null);
    setIsPaused(false);
  };

  const handleAutoSubmit = () => {
    handleSubmitExam();
  };

  const handleSubmitExam = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    clearInterval(timerRef.current);

    try {
      const durationSeconds = ((testMeta?.durationMinutes || 180) * 60) - timeLeft;
      const headers = { 'Content-Type': 'application/json' };
      if (user?.email) headers['x-user-email'] = user.email;

      const res = await fetch(`/api/tests/${testId}/submit`, {
        method: 'POST',
        headers,
        body: JSON.stringify({
          answers,
          startedAt: new Date(startTimeRef.current).toISOString(),
          durationSeconds: Math.max(durationSeconds, 1),
          sectionTime: categoryTime,
        }),
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to submit exam');

      setResultData(data);
      setShowResultModal(true);
      clearSavedProgress();

      try {
        confetti({ particleCount: 70, spread: 60, origin: { y: 0.6 } });
      } catch (e) {}
    } catch (err) {
      alert('Submission Error: ' + err.message);
    } finally {
      setIsSubmitting(false);
    }
  };

  // Status counters for question palette
  const answeredCount = Object.keys(answers).length;
  const reviewCount = markedForReview.size;

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex flex-col items-center justify-center p-4">
        <div className="w-10 h-10 border-3 border-blue-600 border-t-transparent rounded-full animate-spin mb-4"></div>
        <p className="text-sm font-semibold text-slate-600 dark:text-slate-400">Loading Official TSPLRB CBT Exam Canvas...</p>
      </div>
    );
  }

  if (error?.isLocked) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex items-center justify-center p-4">
        <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-8 text-center shadow-lg">
          <div className="w-12 h-12 bg-amber-50 dark:bg-amber-950/60 text-amber-600 rounded-xl flex items-center justify-center mx-auto mb-4 border border-amber-200 dark:border-amber-800">
            <Lock className="w-6 h-6" />
          </div>
          <h2 className="text-xl font-bold mb-2">Paper Locked</h2>
          <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
            {error.message || 'This 200-question full exam requires full access. Unlock all exams for ₹99.'}
          </p>
          <div className="space-y-3">
            <button
              onClick={() => setShowCheckoutModal(true)}
              className="block w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl transition-colors text-xs shadow-xs cursor-pointer"
            >
              Unlock Full Access for ₹99
            </button>
            <Link
              to="/dashboard"
              className="block w-full bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 hover:bg-slate-200 py-2.5 rounded-xl transition-colors text-xs font-semibold"
            >
              Back to Dashboard
            </Link>
          </div>
        </div>

        <CheckoutModal
          isOpen={showCheckoutModal}
          onClose={() => setShowCheckoutModal(false)}
          onSuccess={() => window.location.reload()}
        />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-100 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col font-sans transition-colors">
      
      {/* 1. TOP EXAM HEADER */}
      <header className="sticky top-0 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 px-3 sm:px-6 py-2 sm:py-2.5 transition-colors">
        <div className="max-w-[1440px] mx-auto flex items-center justify-between gap-1 sm:gap-3">
          
          {/* Back Button & Title */}
          <div className="flex items-center gap-1.5 sm:gap-3 flex-shrink-0">
            <button
              onClick={handleAttemptExit}
              title="Pause and Exit Test"
              className="p-1 sm:p-1.5 rounded-lg border border-slate-200 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-600 dark:text-slate-300 transition-colors cursor-pointer"
            >
              <ArrowLeft className="w-3.5 h-3.5 sm:w-4 sm:h-4" />
            </button>
            <div>
              <div className="flex items-center gap-1.5 sm:gap-2">
                <span className="font-bold text-xs sm:text-sm text-slate-900 dark:text-white truncate max-w-[100px] xs:max-w-[140px] sm:max-w-md">
                  {testId === 'demo-test-50' ? 'TSPLRB SI Free Demo' : testMeta?.testId || 'TSPLRB SI Mock Test'}
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800 hidden sm:inline">
                  Page {currentPage}/{totalPages} (Q{startIndex + 1}–{Math.min(startIndex + QUESTIONS_PER_PAGE, totalQuestions)})
                </span>
              </div>
            </div>
          </div>

          {/* Center: Live Timer & Pause */}
          {!reviewMode && (
            <div className="flex items-center gap-1 sm:gap-2 flex-shrink-0">
              <div className={`flex items-center gap-1 sm:gap-1.5 px-2 sm:px-3 py-1 sm:py-1.5 rounded-xl border font-mono font-bold text-xs sm:text-sm transition-colors ${
                timeLeft < 600
                  ? 'bg-rose-50 dark:bg-rose-950/60 border-rose-300 text-rose-600 dark:text-rose-400 animate-pulse'
                  : 'bg-slate-50 dark:bg-slate-950 border-slate-200 dark:border-slate-800 text-slate-800 dark:text-slate-200'
              }`}>
                <Clock className="w-3 h-3 sm:w-3.5 sm:h-3.5" />
                <span>{isPaused ? 'PAUSED' : formatTime(timeLeft)}</span>
              </div>

              <button
                onClick={isPaused ? handleResumeTest : handlePauseTest}
                className="p-1 sm:p-1.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900 hover:bg-slate-100 text-slate-700 dark:text-slate-300 transition-colors text-xs font-semibold flex items-center gap-1 cursor-pointer"
              >
                {isPaused ? <Play className="w-3.5 h-3.5 text-emerald-600 fill-current" /> : <Pause className="w-3.5 h-3.5 text-slate-700 dark:text-slate-300 fill-current" />}
                <span className="hidden sm:inline">{isPaused ? 'Resume' : 'Pause'}</span>
              </button>
            </div>
          )}

          {/* Right: Language Toggle, Theme & Palette */}
          <div className="flex items-center gap-1 sm:gap-2 flex-shrink-0">
            
            {/* Language Switcher */}
            <div className="hidden sm:flex items-center bg-slate-100 dark:bg-slate-950 p-0.5 rounded-lg border border-slate-200 dark:border-slate-800 text-[11px] font-semibold">
              <button
                onClick={() => setLangMode('dual')}
                className={`px-2 py-0.5 rounded-md cursor-pointer transition-colors ${langMode === 'dual' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs font-bold' : 'text-slate-500'}`}
              >
                Dual
              </button>
              <button
                onClick={() => setLangMode('en')}
                className={`px-2 py-0.5 rounded-md cursor-pointer transition-colors ${langMode === 'en' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs font-bold' : 'text-slate-500'}`}
              >
                EN
              </button>
              <button
                onClick={() => setLangMode('te')}
                className={`px-2 py-0.5 rounded-md cursor-pointer transition-colors ${langMode === 'te' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs font-bold' : 'text-slate-500'}`}
              >
                తెలుగు
              </button>
            </div>

            {/* Theme Toggle */}
            <button
              onClick={toggleTheme}
              className="w-7 h-7 sm:w-8 sm:h-8 rounded-lg border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 flex items-center justify-center hover:bg-slate-100 transition-colors cursor-pointer"
            >
              {theme === 'dark' ? <Sun className="w-3 h-3 sm:w-3.5 sm:h-3.5 text-amber-400" /> : <Moon className="w-3 h-3 sm:w-3.5 sm:h-3.5 text-slate-700" />}
            </button>

            {/* Questions Palette Toggle (Mobile & Desktop) */}
            <button
              onClick={() => setPaletteOpen(!paletteOpen)}
              className="flex items-center gap-1 sm:gap-1.5 px-2.5 sm:px-3 py-1 sm:py-1.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold transition-colors shadow-xs cursor-pointer"
            >
              <LayoutGrid className="w-3 h-3 sm:w-3.5 sm:h-3.5" />
              <span>Palette</span>
              <span className="bg-blue-800/80 px-1.5 py-0.2 rounded-full text-[10px]">{answeredCount}</span>
            </button>

          </div>

        </div>
      </header>

      {/* 2. EXAM CONTENT CANVAS (BLURRED & LOCKED WHEN PAUSED OR PROMPTED) */}
      <div className={`flex-1 flex flex-col transition-all duration-300 ${
        (isPaused || showExitModal || resumePrompt)
          ? 'filter blur-2xl select-none pointer-events-none opacity-20'
          : ''
      }`}>

        {/* HORIZONTALLY EXTENDED CATEGORIES AT TOP OF QUIZ (Item 8) */}
        <div className="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-3 sm:px-6 py-2 sm:py-2.5 transition-colors">
          <div className="max-w-[1440px] mx-auto">
            <div className="grid grid-cols-3 gap-1.5 sm:gap-2.5 w-full">
              {sectionRanges.map((sec) => {
                const isCurrent = currentSection.key === sec.key;
                let ansInSec = 0;
                for (let q = sec.startQ; q <= sec.endQ; q++) {
                  if (answers[q] !== undefined) ansInSec++;
                }

                return (
                  <button
                    key={sec.key}
                    onClick={() => handleJumpToQuestion(sec.startQ)}
                    className={`w-full p-2 sm:p-3 rounded-xl border text-left transition-all cursor-pointer flex flex-col sm:flex-row items-start sm:items-center justify-between shadow-xs ${
                      isCurrent
                        ? 'bg-blue-50/80 dark:bg-blue-950/60 border-blue-500 ring-1 ring-blue-500/30'
                        : 'bg-slate-50 dark:bg-slate-950 border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
                    }`}
                  >
                    <div className="min-w-0 flex-1">
                      <div className="flex items-center gap-1 sm:gap-1.5">
                        <span className={`w-1.5 h-1.5 sm:w-2 sm:h-2 rounded-full flex-shrink-0 ${isCurrent ? 'bg-blue-600 animate-pulse' : 'bg-slate-400'}`} />
                        <span className={`font-bold text-[11px] sm:text-sm truncate ${isCurrent ? 'text-blue-900 dark:text-blue-200' : 'text-slate-800 dark:text-slate-200'}`}>
                          {sec.shortName}
                        </span>
                        <span className="text-[9px] sm:text-[10px] text-slate-400 font-mono hidden xs:inline">
                          (Q{sec.startQ}–{sec.endQ})
                        </span>
                      </div>
                      <div className="text-[10px] sm:text-[11px] text-slate-500 dark:text-slate-400 mt-0.5 truncate hidden sm:block">
                        {sec.name}
                      </div>
                    </div>
                    <div className="text-right flex-shrink-0 mt-1 sm:mt-0 sm:ml-2">
                      <span className={`text-[9px] sm:text-[10px] font-bold px-1.5 sm:px-2 py-0.5 rounded-full border ${
                        ansInSec === sec.total 
                          ? 'bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 border-emerald-300 dark:border-emerald-700'
                          : ansInSec > 0
                          ? 'bg-blue-50 dark:bg-blue-950/40 text-blue-700 dark:text-blue-300 border-blue-200 dark:border-blue-800'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400 border-slate-200 dark:border-slate-700'
                      }`}>
                        {ansInSec}/{sec.total}
                      </span>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* MAIN EXAM CANVAS (10 QUESTIONS PER PAGE) */}
        <main className="flex-1 max-w-[1440px] w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          
          {/* LEFT: 10 Questions Column (8 Columns) */}
          <div className="lg:col-span-8 space-y-6">
            
            {/* Page Header Bar */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 flex items-center justify-between shadow-xs">
              <div>
                <h1 className="font-bold text-sm sm:text-base text-slate-900 dark:text-white">
                  Questions {startIndex + 1} to {Math.min(startIndex + QUESTIONS_PER_PAGE, totalQuestions)} of {totalQuestions}
                </h1>
                <p className="text-xs text-slate-500 dark:text-slate-400">Page {currentPage} of {totalPages}</p>
              </div>

              <div className="flex items-center gap-1.5">
                <button
                  onClick={() => handleGoToPage(currentPage - 1)}
                  disabled={currentPage <= 1}
                  className="p-1.5 rounded-lg border border-slate-200 dark:border-slate-800 disabled:opacity-30 hover:bg-slate-100 transition-colors cursor-pointer"
                >
                  <ChevronLeft className="w-4 h-4" />
                </button>
                <button
                  onClick={() => handleGoToPage(currentPage + 1)}
                  disabled={currentPage >= totalPages}
                  className="p-1.5 rounded-lg border border-slate-200 dark:border-slate-800 disabled:opacity-30 hover:bg-slate-100 transition-colors cursor-pointer"
                >
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>

            {/* Questions List */}
            {currentQuestions.map((q) => {
              const qNum = q.id || q.qNumber;
              const selectedOpt = answers[qNum];
              const isReviewed = markedForReview.has(qNum);
              const isHighlighted = highlightedQ === qNum;

              // Review result mapping (if test finished)
              const reviewQ = resultData?.reviewQuestions?.find(rq => (rq.id || rq.qNumber) === qNum);

              return (
                <div
                  key={qNum}
                  id={`question-card-${qNum}`}
                  className={`bg-white dark:bg-slate-900 border rounded-2xl p-5 sm:p-6 transition-all shadow-xs ${
                    isHighlighted
                      ? 'border-blue-500 ring-2 ring-blue-500/20'
                      : 'border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
                  }`}
                >
                  {/* Question Metadata */}
                  <div className="flex items-center justify-between pb-3 mb-4 border-b border-slate-100 dark:border-slate-800">
                    <div className="flex items-center gap-2">
                      <span className="w-7 h-7 rounded-lg bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-bold text-xs flex items-center justify-center">
                        Q {qNum}
                      </span>
                      <span className="text-xs font-semibold text-blue-600 dark:text-blue-400">
                        {q.section || 'General'}
                      </span>
                      {reviewMode && q.topic && (
                        <span className="text-[11px] text-slate-400 hidden sm:inline">• {q.topic}</span>
                      )}
                    </div>

                    <div className="flex items-center gap-2">
                      {!reviewMode ? (
                        <>
                          <button
                            onClick={() => handleToggleReview(qNum)}
                            className={`flex items-center gap-1 text-xs font-semibold px-2.5 py-1 rounded-lg border transition-colors cursor-pointer ${
                              isReviewed
                                ? 'bg-purple-50 dark:bg-purple-950/60 border-purple-300 text-purple-700 dark:text-purple-300'
                                : 'bg-slate-50 dark:bg-slate-950 border-slate-200 dark:border-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-100'
                            }`}
                          >
                            <Bookmark className={`w-3.5 h-3.5 ${isReviewed ? 'fill-current' : ''}`} />
                            <span>{isReviewed ? 'Marked for Review' : 'Review'}</span>
                          </button>
                          <span className="text-[11px] font-mono text-slate-400">+1.0 / -0.20</span>
                        </>
                      ) : (
                        <span className={`text-xs font-bold px-2.5 py-1 rounded-lg border ${
                          reviewQ?.isCorrect
                            ? 'bg-emerald-50 text-emerald-700 border-emerald-300'
                            : reviewQ?.isWrong
                            ? 'bg-rose-50 text-rose-700 border-rose-300'
                            : 'bg-slate-100 text-slate-600 border-slate-300'
                        }`}>
                          {reviewQ?.isCorrect ? '+1.0 Correct' : reviewQ?.isWrong ? '-0.20 Wrong' : '0.0 Unanswered'}
                        </span>
                      )}
                    </div>
                  </div>

                  {/* Question Text (Bilingual with Structured Line-Breaks) */}
                  <div className="space-y-3 mb-5">
                    {(langMode === 'dual' || langMode === 'en') && q.question_en && (
                      <p className="text-sm font-semibold text-slate-900 dark:text-white leading-relaxed whitespace-pre-line">
                        {formatQuestionText(q.question_en)}
                      </p>
                    )}
                    {(langMode === 'dual' || langMode === 'te') && q.question_te && (
                      <p className="text-sm text-slate-800 dark:text-slate-200 leading-relaxed font-telugu whitespace-pre-line">
                        {formatQuestionText(q.question_te)}
                      </p>
                    )}
                  </div>

                  {/* Options */}
                  <div className="space-y-2.5 mb-4">
                    {(q.options || []).map((opt, optIdx) => {
                      const isSelected = selectedOpt === optIdx;
                      const optLabel = String.fromCharCode(65 + optIdx); // A, B, C, D

                      // Review styling
                      let optClasses = 'border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 bg-white dark:bg-slate-900';
                      if (!reviewMode) {
                        if (isSelected) {
                          optClasses = 'border-blue-600 dark:border-blue-500 bg-blue-50/60 dark:bg-blue-950/40 text-blue-900 dark:text-blue-100 ring-1 ring-blue-600';
                        }
                      } else {
                        const isCorrectOption = reviewQ?.correctOption === optIdx;
                        const wasChosenByUser = reviewQ?.selectedOption === optIdx;

                        if (isCorrectOption) {
                          optClasses = 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-900 dark:text-emerald-100 ring-2 ring-emerald-500';
                        } else if (wasChosenByUser && !isCorrectOption) {
                          optClasses = 'border-rose-500 bg-rose-50 dark:bg-rose-950/60 text-rose-900 dark:text-rose-100 ring-2 ring-rose-500';
                        }
                      }

                      return (
                        <div
                          key={optIdx}
                          onClick={() => !reviewMode && handleSelectOption(qNum, optIdx)}
                          className={`border rounded-xl p-3 flex items-start gap-3 transition-colors ${reviewMode ? 'cursor-default' : 'cursor-pointer'} ${optClasses}`}
                        >
                          <div className={`w-6 h-6 rounded-lg text-xs font-bold flex items-center justify-center flex-shrink-0 mt-0.5 border ${
                            isSelected
                              ? 'bg-blue-600 border-blue-600 text-white'
                              : 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
                          }`}>
                            {optLabel}
                          </div>
                          <div className="flex-1 text-xs sm:text-sm">
                            {(langMode === 'dual' || langMode === 'en') && opt.text_en && (
                              <div className="font-medium text-slate-800 dark:text-slate-200 whitespace-pre-line">{opt.text_en}</div>
                            )}
                            {(langMode === 'dual' || langMode === 'te') && opt.text_te && (
                              <div className="text-slate-700 dark:text-slate-300 font-telugu mt-0.5 whitespace-pre-line">{opt.text_te}</div>
                            )}
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  {/* Clear Button (If answered and not in review) */}
                  {!reviewMode && selectedOpt !== undefined && (
                    <div className="flex justify-end">
                      <button
                        onClick={() => handleClearAnswer(qNum)}
                        className="text-[11px] text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 font-semibold cursor-pointer"
                      >
                        Clear Response
                      </button>
                    </div>
                  )}

                  {/* Review Mode Explanation */}
                  {reviewMode && reviewQ && (
                    <div className="mt-4 pt-4 border-t border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 p-4 rounded-xl text-xs space-y-2">
                      <div className="font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                        <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                        <span>Official Solution & Explanation:</span>
                      </div>
                      {reviewQ.explanation_en && (
                        <p className="text-slate-700 dark:text-slate-300 leading-relaxed">{reviewQ.explanation_en}</p>
                      )}
                      {reviewQ.explanation_te && (
                        <p className="text-slate-700 dark:text-slate-300 font-telugu leading-relaxed">{reviewQ.explanation_te}</p>
                      )}
                    </div>
                  )}

                </div>
              );
            })}

            {/* Bottom Pagination Bar with Page Buttons & Question Ranges (Item 7) */}
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xs space-y-4">
              <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-800 pb-3">
                <div>
                  <h3 className="font-bold text-xs sm:text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
                    <Layers className="w-4 h-4 text-blue-600" />
                    <span>Question Pages Navigation</span>
                  </h3>
                  <p className="text-[11px] text-slate-500 dark:text-slate-400">
                    Click any page button below to navigate directly
                  </p>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-semibold text-slate-500">
                    Current: <strong className="text-slate-900 dark:text-white">Page {currentPage} of {totalPages}</strong>
                  </span>
                  <span className="text-slate-300 dark:text-slate-700">|</span>
                  <span className="text-xs font-bold text-emerald-600 dark:text-emerald-400">
                    {answeredCount}/{totalQuestions} Answered
                  </span>
                </div>
              </div>

              {/* All page number buttons with question range in small text */}
              <div className="grid grid-cols-4 sm:grid-cols-5 md:grid-cols-10 gap-2">
                {Array.from({ length: totalPages }, (_, i) => i + 1).map((p) => {
                  const startQ = (p - 1) * QUESTIONS_PER_PAGE + 1;
                  const endQ = Math.min(p * QUESTIONS_PER_PAGE, totalQuestions);
                  const isActive = p === currentPage;

                  let pageAnsCount = 0;
                  for (let q = startQ; q <= endQ; q++) {
                    if (answers[q] !== undefined) pageAnsCount++;
                  }
                  const pageTotalQ = endQ - startQ + 1;

                  return (
                    <button
                      key={p}
                      onClick={() => handleGoToPage(p)}
                      className={`py-2 px-1 rounded-xl border text-center transition-all cursor-pointer flex flex-col items-center justify-center ${
                        isActive
                          ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 border-slate-900 dark:border-white shadow-md ring-2 ring-blue-500/40'
                          : pageAnsCount === pageTotalQ
                          ? 'bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 border-emerald-300 dark:border-emerald-800 hover:bg-emerald-100'
                          : pageAnsCount > 0
                          ? 'bg-blue-50/60 dark:bg-blue-950/30 text-blue-800 dark:text-blue-300 border-blue-200 dark:border-blue-800 hover:bg-blue-100'
                          : 'bg-slate-50 dark:bg-slate-950 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-800'
                      }`}
                    >
                      <span className="font-extrabold text-xs">Page {p}</span>
                      <span className={`text-[9px] mt-0.5 ${isActive ? 'text-slate-300 dark:text-slate-600' : 'text-slate-500 dark:text-slate-400'}`}>
                        Q {startQ}–{endQ}
                      </span>
                      <span className={`text-[8px] font-bold mt-0.5 ${
                        isActive ? 'opacity-80' : pageAnsCount === pageTotalQ ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-400'
                      }`}>
                        {pageAnsCount}/{pageTotalQ}
                      </span>
                    </button>
                  );
                })}
              </div>

              {/* Prev and Next navigation buttons */}
              <div className="flex items-center justify-between pt-2">
                <button
                  onClick={() => handleGoToPage(currentPage - 1)}
                  disabled={currentPage <= 1}
                  className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 disabled:opacity-30 text-slate-800 dark:text-slate-200 text-xs font-bold px-4 py-2 rounded-xl transition-colors cursor-pointer flex items-center gap-1.5"
                >
                  <ChevronLeft className="w-4 h-4" />
                  <span>Previous Page</span>
                </button>

                <button
                  onClick={() => handleGoToPage(currentPage + 1)}
                  disabled={currentPage >= totalPages}
                  className="bg-blue-600 hover:bg-blue-700 disabled:opacity-30 text-white text-xs font-bold px-4 py-2 rounded-xl transition-colors cursor-pointer shadow-xs flex items-center gap-1.5"
                >
                  <span>Next Page</span>
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>
            </div>

          </div>

          {/* RIGHT: Questions Palette (4 Columns on Desktop, Drawer on Mobile) */}
          <aside className={`lg:col-span-4 lg:sticky lg:top-16 lg:self-start z-20 ${
            paletteOpen
              ? 'fixed inset-0 z-50 bg-black/40 p-3 sm:p-4 flex items-center justify-center lg:p-0 lg:bg-transparent'
              : 'hidden lg:block'
          }`}>
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 sm:p-5 shadow-xs w-full max-w-[calc(100vw-1.5rem)] sm:max-w-md lg:max-w-none max-h-[85vh] lg:max-h-[calc(100vh-5.5rem)] flex flex-col">
              
              {/* Palette Header */}
              <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-100 dark:border-slate-800">
                <div>
                  <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-1.5">
                    <LayoutGrid className="w-4 h-4 text-blue-600" />
                    <span>Questions Palette</span>
                  </h3>
                  <p className="text-[11px] text-slate-400">{answeredCount}/{totalQuestions} Answered</p>
                </div>
                <button
                  onClick={() => setPaletteOpen(false)}
                  className="lg:hidden p-1 text-slate-400 hover:text-slate-600 cursor-pointer"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Status Legend */}
              <div className="grid grid-cols-2 gap-2 text-[10px] text-slate-500 mb-3 bg-slate-50 dark:bg-slate-950 p-2.5 rounded-xl border border-slate-100 dark:border-slate-800">
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                  <span>Answered ({answeredCount})</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-purple-500"></span>
                  <span>Review ({reviewCount})</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-rose-500"></span>
                  <span>Not Answered ({visited.size - answeredCount > 0 ? visited.size - answeredCount : 0})</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-slate-200 dark:bg-slate-700"></span>
                  <span>Unvisited ({totalQuestions - visited.size})</span>
                </div>
              </div>

              {/* Questions Buttons Grid */}
              <div className="flex-1 overflow-y-auto pr-1 grid grid-cols-5 gap-1.5 mb-4">
                {Array.from({ length: totalQuestions }, (_, i) => i + 1).map((qNum) => {
                  const isAnswered = answers[qNum] !== undefined;
                  const isReviewed = markedForReview.has(qNum);
                  const isCurrent = Math.floor((qNum - 1) / QUESTIONS_PER_PAGE) + 1 === currentPage;

                  let btnClasses = 'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-700';
                  if (isAnswered) {
                    btnClasses = 'bg-emerald-600 text-white border-emerald-600 font-bold';
                  } else if (isReviewed) {
                    btnClasses = 'bg-purple-600 text-white border-purple-600 font-bold';
                  } else if (visited.has(qNum)) {
                    btnClasses = 'bg-rose-500 text-white border-rose-500 font-bold';
                  }

                  return (
                    <button
                      key={qNum}
                      onClick={() => handleJumpToQuestion(qNum)}
                      className={`h-8 rounded-lg text-xs font-semibold border transition-all cursor-pointer flex items-center justify-center ${btnClasses} ${
                        isCurrent ? 'ring-2 ring-blue-500' : ''
                      }`}
                    >
                      {qNum}
                    </button>
                  );
                })}
              </div>

              {/* Submit Button */}
              {!reviewMode ? (
                <button
                  onClick={handleSubmitExam}
                  disabled={isSubmitting}
                  className="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
                >
                  <Check className="w-4 h-4" />
                  <span>Submit & Finish Examination</span>
                </button>
              ) : (
                <Link
                  to="/dashboard"
                  className="w-full text-center bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-bold text-xs py-2.5 rounded-xl transition-colors shadow-xs"
                >
                  Back to Dashboard
                </Link>
              )}

            </div>
          </aside>

        </div>
      </main>
      </div>

      {/* 5. PAUSED EXAMINATION ANTI-CHEAT OVERLAY */}
      {isPaused && !showExitModal && !resumePrompt && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-3 sm:p-4">
          <div className="max-w-[calc(100vw-1.5rem)] sm:max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl sm:rounded-3xl p-5 sm:p-8 text-center shadow-2xl relative animate-in fade-in zoom-in-95 duration-200">
            
            {/* Animated Pulsing Pause Ring */}
            <div className="relative w-16 h-16 mx-auto mb-4 flex items-center justify-center">
              <div className="absolute inset-0 rounded-2xl bg-amber-500/20 animate-ping" />
              <div className="relative w-16 h-16 bg-amber-50 dark:bg-amber-950/60 border border-amber-200 dark:border-amber-800 rounded-2xl flex items-center justify-center text-amber-600 dark:text-amber-400 shadow-xs">
                <Pause className="w-8 h-8 fill-current" />
              </div>
            </div>

            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-50 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300 text-xs font-bold border border-amber-200 dark:border-amber-800 mb-2.5">
              <span>Examination Paused</span>
            </div>

            <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-2">
              Quiz is on Pause
            </h2>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
              Questions and answers are blurred to maintain official examination integrity. The timer is stopped and all your responses are securely preserved.
            </p>

            {/* Quick Metrics Snapshot */}
            <div className="grid grid-cols-3 gap-2 bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-3.5 mb-6 text-center">
              <div>
                <div className="text-[10px] text-slate-400 font-semibold uppercase tracking-wider">Time Left</div>
                <div className="font-mono font-bold text-xs text-slate-900 dark:text-white mt-0.5">{formatTime(timeLeft)}</div>
              </div>
              <div className="border-x border-slate-200 dark:border-slate-800">
                <div className="text-[10px] text-slate-400 font-semibold uppercase tracking-wider">Answered</div>
                <div className="font-bold text-xs text-emerald-600 dark:text-emerald-400 mt-0.5">{answeredCount}/{totalQuestions}</div>
              </div>
              <div>
                <div className="text-[10px] text-slate-400 font-semibold uppercase tracking-wider">Marked</div>
                <div className="font-bold text-xs text-amber-600 dark:text-amber-400 mt-0.5">{reviewCount}</div>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="space-y-2.5">
              <button
                onClick={handleResumeTest}
                className="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-3 rounded-xl transition-all shadow-md flex items-center justify-center gap-2 cursor-pointer hover:scale-[1.01]"
              >
                <Play className="w-4 h-4 fill-current" />
                <span>Resume Examination</span>
              </button>

              <button
                onClick={handleAttemptExit}
                className="w-full bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 font-semibold text-xs py-2.5 rounded-xl transition-colors cursor-pointer"
              >
                Save Progress & Exit to Dashboard
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 6. PAUSE & EXIT SAFETY CONFIRMATION MODAL */}
      {showExitModal && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-3 sm:p-4">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl sm:rounded-3xl p-5 sm:p-8 max-w-[calc(100vw-1.5rem)] sm:max-w-md w-full shadow-2xl text-center">
            <div className="w-14 h-14 bg-amber-50 dark:bg-amber-950/60 text-amber-600 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-amber-200 dark:border-amber-800">
              <Pause className="w-6 h-6 fill-current" />
            </div>
            
            <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-2">
              Pause & Exit Examination?
            </h2>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
              You have an active exam in progress. Your answers and remaining time will be saved automatically so you can resume anytime.
            </p>

            <div className="grid grid-cols-3 gap-2 mb-6 bg-slate-50 dark:bg-slate-950 p-3 rounded-xl border border-slate-100 dark:border-slate-800 text-xs">
              <div>
                <div className="text-[10px] text-slate-400">Answered</div>
                <div className="font-bold text-emerald-600">{answeredCount}/{totalQuestions}</div>
              </div>
              <div>
                <div className="text-[10px] text-slate-400">Time Left</div>
                <div className="font-bold text-slate-800 dark:text-slate-200">{formatTime(timeLeft)}</div>
              </div>
              <div>
                <div className="text-[10px] text-slate-400">Current Page</div>
                <div className="font-bold text-blue-600">P{currentPage}/{totalPages}</div>
              </div>
            </div>

            <div className="space-y-2.5">
              <button
                onClick={handleResumeTest}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Continue Taking Exam</span>
              </button>

              <button
                onClick={handleConfirmExit}
                className="w-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 font-bold text-xs py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <Save className="w-3.5 h-3.5" />
                <span>Save Progress & Exit to Dashboard</span>
              </button>

              <button
                onClick={handleDiscardAndQuit}
                className="w-full text-rose-600 hover:text-rose-700 text-xs font-semibold py-1.5 cursor-pointer"
              >
                Discard attempt and start fresh next time
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 6. RESUME PROMPT MODAL (When opening an exam with saved progress) */}
      {resumePrompt && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 sm:p-8 max-w-md w-full shadow-2xl text-center">
            <div className="w-14 h-14 bg-blue-50 dark:bg-blue-950/60 text-blue-600 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-blue-200 dark:border-blue-800">
              <RotateCcw className="w-6 h-6" />
            </div>
            
            <h2 className="text-xl font-bold text-slate-900 dark:text-white mb-2">
              Resume Previous Attempt?
            </h2>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
              We found saved progress from your previous session ({Object.keys(resumePrompt.answers || {}).length} questions answered). Would you like to pick up where you left off?
            </p>

            <div className="space-y-2.5">
              <button
                onClick={handleAcceptResume}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Resume Saved Exam</span>
              </button>

              <button
                onClick={handleDeclineResume}
                className="w-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 font-bold text-xs py-2.5 rounded-xl transition-colors cursor-pointer"
              >
                Start Fresh Attempt
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 7. RESULT / SCORECARD MODAL */}
      {showResultModal && resultData && (
        <div className="fixed inset-0 z-50 bg-black/70 backdrop-blur-sm flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl sm:rounded-3xl p-5 sm:p-8 max-w-[calc(100vw-1.5rem)] sm:max-w-xl w-full shadow-2xl text-center my-4 sm:my-8">
            <div className="w-16 h-16 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-emerald-200 dark:border-emerald-800">
              <Trophy className="w-8 h-8" />
            </div>

            <h2 className="text-2xl font-black text-slate-900 dark:text-white mb-1">Examination Completed!</h2>
            <p className="text-xs text-slate-500 dark:text-slate-400 mb-6">TSPLRB Sub-Inspector Preliminary Written Test Simulation</p>

            {/* Scorecard Hero */}
            <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 mb-6">
              <div className="text-xs font-semibold text-slate-500 uppercase">Your Final Score</div>
              <div className="text-4xl font-black text-slate-900 dark:text-white mt-1">
                {resultData.totalScore} <span className="text-base text-slate-400 font-normal">/ {resultData.totalMarks}</span>
              </div>
              <div className="mt-2 inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
                <span>Accuracy: {resultData.accuracyPercent}%</span>
              </div>

              {/* Breakdown Grid */}
              <div className="grid grid-cols-3 gap-2 mt-5 pt-4 border-t border-slate-200 dark:border-slate-800 text-xs">
                <div className="text-emerald-600">
                  <div className="text-[10px] text-slate-400 uppercase">Correct</div>
                  <div className="font-black text-base mt-0.5">{resultData.correctCount}</div>
                  <div className="text-[9px] text-slate-400">+1.0 each</div>
                </div>
                <div className="text-rose-600">
                  <div className="text-[10px] text-slate-400 uppercase">Wrong</div>
                  <div className="font-black text-base mt-0.5">{resultData.wrongCount}</div>
                  <div className="text-[9px] text-slate-400">-0.20 each</div>
                </div>
                <div className="text-slate-500">
                  <div className="text-[10px] text-slate-400 uppercase">Unanswered</div>
                  <div className="font-black text-base mt-0.5">{resultData.unansweredCount}</div>
                  <div className="text-[9px] text-slate-400">0.0</div>
                </div>
              </div>

              {/* Category Qualifying Cut-off Status */}
              <div className="mt-4 pt-3 border-t border-slate-200 dark:border-slate-800">
                <div className="text-[10px] font-bold text-slate-500 uppercase tracking-wider mb-2">Official Category Qualifying Status</div>
                <div className="grid grid-cols-3 gap-1.5 text-center text-xs">
                  {(() => {
                    const isDemo = resultData.totalMarks === 50;
                    const ocReq = isDemo ? 15 : 60;
                    const bcReq = isDemo ? 12.5 : 50;
                    const scReq = isDemo ? 10 : 40;
                    return (
                      <>
                        <div className={`p-2 rounded-xl border ${resultData.totalScore >= ocReq ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-700 text-emerald-800 dark:text-emerald-300' : 'bg-slate-100/60 dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-500'}`}>
                          <div className="text-[10px] font-semibold text-slate-400">OC (Cut-off {ocReq})</div>
                          <div className="font-bold text-xs mt-0.5">{resultData.totalScore >= ocReq ? '✓ Qualified' : 'Not Qualified'}</div>
                        </div>
                        <div className={`p-2 rounded-xl border ${resultData.totalScore >= bcReq ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-700 text-emerald-800 dark:text-emerald-300' : 'bg-slate-100/60 dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-500'}`}>
                          <div className="text-[10px] font-semibold text-slate-400">BC (Cut-off {bcReq})</div>
                          <div className="font-bold text-xs mt-0.5">{resultData.totalScore >= bcReq ? '✓ Qualified' : 'Not Qualified'}</div>
                        </div>
                        <div className={`p-2 rounded-xl border ${resultData.totalScore >= scReq ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-700 text-emerald-800 dark:text-emerald-300' : 'bg-slate-100/60 dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-500'}`}>
                          <div className="text-[10px] font-semibold text-slate-400">SC/ST (Cut-off {scReq})</div>
                          <div className="font-bold text-xs mt-0.5">{resultData.totalScore >= scReq ? '✓ Qualified' : 'Not Qualified'}</div>
                        </div>
                      </>
                    );
                  })()}
                </div>
              </div>
            </div>

            {/* Sectional Performance & Category Time Breakdown (Item 9) */}
            {resultData.sectionBreakdown && (
              <div className="space-y-2 mb-6 text-left text-xs">
                <div className="font-bold text-slate-900 dark:text-white mb-2 flex items-center justify-between">
                  <span>Sectional Score & Time Breakdown:</span>
                  <span className="text-[10px] text-slate-400 font-normal">Tracked per category</span>
                </div>
                {Object.entries(resultData.sectionBreakdown).map(([k, sec]) => {
                  const secSeconds = sec.timeSpentSeconds !== undefined ? sec.timeSpentSeconds : (categoryTime[k] || 0);
                  const formatSecTime = (s) => {
                    const m = Math.floor(s / 60);
                    const remS = s % 60;
                    if (m >= 60) {
                      return `${Math.floor(m / 60)}h ${m % 60}m ${remS}s`;
                    }
                    return `${m}m ${remS}s`;
                  };

                  return (
                    <div key={k} className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 p-3 rounded-xl flex items-center justify-between">
                      <div>
                        <div className="font-bold text-slate-800 dark:text-slate-200">{sec.name}</div>
                        <div className="text-[10px] text-slate-400 mt-0.5">
                          {sec.correct} Correct • {sec.wrong} Wrong of {sec.total} Qs
                        </div>
                      </div>
                      <div className="text-right">
                        <div className="font-bold text-slate-900 dark:text-white">
                          {sec.score.toFixed(1)} Marks
                        </div>
                        <div className="text-[10px] text-blue-600 dark:text-blue-400 font-mono font-semibold mt-0.5">
                          ⏱ {formatSecTime(secSeconds)}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}

            {/* Action Buttons */}
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={() => {
                  setShowResultModal(false);
                  setReviewMode(true);
                  setCurrentPage(1);
                  window.scrollTo({ top: 0, behavior: 'smooth' });
                }}
                className="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <BookOpen className="w-3.5 h-3.5" />
                <span>Review All Solutions</span>
              </button>

              <Link
                to="/dashboard"
                className="bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 font-bold text-xs py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-1.5"
              >
                <span>Go to Dashboard</span>
              </Link>
            </div>

          </div>
        </div>
      )}

    </div>
  );
}
