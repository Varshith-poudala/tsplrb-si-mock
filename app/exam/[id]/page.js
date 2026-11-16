'use client';

import { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { useSession } from 'next-auth/react';
import Link from 'next/link';
import { 
  Clock, Shield, Globe, Menu, X, CheckCircle2, Bookmark, ArrowLeft, ArrowRight, 
  RotateCcw, AlertTriangle, Trophy, Award, Lock, BookOpen, ChevronLeft, ChevronRight,
  Layers, Check, Pause, Play, Save, AlertCircle, HelpCircle, LayoutGrid
} from 'lucide-react';
import confetti from 'canvas-confetti';
import ThemeToggle from '@/components/ThemeToggle';

const QUESTIONS_PER_PAGE = 10;

export default function ExamPage() {
  const params = useParams();
  const router = useRouter();
  const { data: session } = useSession();
  const testId = params?.id || 'demo-test-50';

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [testMeta, setTestMeta] = useState(null);
  const [questions, setQuestions] = useState([]);

  // Pagination State (10 Questions Per Page)
  const [currentPage, setCurrentPage] = useState(1);
  const [highlightedQ, setHighlightedQ] = useState(null);

  // Exam Progress State
  const [answers, setAnswers] = useState({}); // { [qNum]: selectedOptionIndex }
  const [markedForReview, setMarkedForReview] = useState(new Set());
  const [visited, setVisited] = useState(new Set());

  // Mobile Drawer & Language State
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [paletteSectionFilter, setPaletteSectionFilter] = useState('all');
  const [langMode, setLangMode] = useState('dual'); // 'dual' | 'en' | 'te'
  const [timeLeft, setTimeLeft] = useState(180 * 60);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Pause & Exit Modal States
  const [isPaused, setIsPaused] = useState(false);
  const [showExitModal, setShowExitModal] = useState(false);
  const [resumePrompt, setResumePrompt] = useState(null); // Saved attempt data prompt

  // Result / Review State
  const [showResultModal, setShowResultModal] = useState(false);
  const [resultData, setResultData] = useState(null);
  const [reviewMode, setReviewMode] = useState(false);

  // Timer Ref
  const timerRef = useRef(null);
  const startTimeRef = useRef(Date.now());
  const mainContentRef = useRef(null);

  // Helper to persist current progress
  const saveProgressToStorage = useCallback((customAnswers, customMarked, customVisited, customTimeLeft, customPage) => {
    try {
      const storageKey = `exam_progress_${testId}`;
      const payload = {
        testId,
        answers: customAnswers || answers,
        markedForReview: Array.from(customMarked || markedForReview),
        visited: Array.from(customVisited || visited),
        timeLeft: customTimeLeft !== undefined ? customTimeLeft : timeLeft,
        currentPage: customPage || currentPage,
        savedAt: new Date().toISOString(),
      };
      localStorage.setItem(storageKey, JSON.stringify(payload));
    } catch (e) {
      console.warn('Could not save exam progress to storage:', e);
    }
  }, [testId, answers, markedForReview, visited, timeLeft, currentPage]);

  // Clear progress helper
  const clearSavedProgress = useCallback(() => {
    try {
      localStorage.removeItem(`exam_progress_${testId}`);
    } catch (e) {}
  }, [testId]);

  // 1. Fetch Sanitized Questions (Zero-Inspect Protection)
  useEffect(() => {
    async function fetchQuestions() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`/api/tests/${testId}/questions`);
        const data = await res.json();

        if (res.status === 402) {
          setError({ isLocked: true, message: data.message });
          setLoading(false);
          return;
        }

        if (!res.ok) {
          throw new Error(data.error || 'Failed to load exam questions');
        }

        setTestMeta(data);
        const fetchedQs = data.questions || [];
        setQuestions(fetchedQs);
        const initialDuration = (data.durationMinutes || 180) * 60;
        setTimeLeft(initialDuration);
        startTimeRef.current = Date.now();

        // Check if there is a saved attempt in localStorage
        try {
          const savedData = localStorage.getItem(`exam_progress_${testId}`);
          if (savedData) {
            const parsed = JSON.parse(savedData);
            if (parsed && parsed.answers && Object.keys(parsed.answers).length > 0) {
              setResumePrompt(parsed);
            } else {
              // Default first 10 visited
              const initialVisited = new Set();
              for (let i = 0; i < Math.min(10, fetchedQs.length); i++) {
                initialVisited.add(fetchedQs[i].qNumber || i + 1);
              }
              setVisited(initialVisited);
            }
          } else {
            const initialVisited = new Set();
            for (let i = 0; i < Math.min(10, fetchedQs.length); i++) {
              initialVisited.add(fetchedQs[i].qNumber || i + 1);
            }
            setVisited(initialVisited);
          }
        } catch (e) {
          console.warn('Failed to parse saved exam progress:', e);
        }
      } catch (err) {
        setError({ message: err.message });
      } finally {
        setLoading(false);
      }
    }

    fetchQuestions();
  }, [testId]);

  // 2. Countdown Timer (Runs only when not paused, not reviewing, and no prompt)
  useEffect(() => {
    if (!loading && questions.length > 0 && !showResultModal && !reviewMode && !isPaused && !showExitModal && !resumePrompt) {
      timerRef.current = setInterval(() => {
        setTimeLeft((prev) => {
          if (prev <= 1) {
            clearInterval(timerRef.current);
            handleSubmitTest(); // Auto-submit when time expires
            return 0;
          }
          const next = prev - 1;
          // Periodically save timer every 10 seconds
          if (next % 10 === 0) {
            saveProgressToStorage(null, null, null, next, null);
          }
          return next;
        });
      }, 1000);
    }
    return () => clearInterval(timerRef.current);
  }, [loading, questions.length, showResultModal, reviewMode, isPaused, showExitModal, resumePrompt, saveProgressToStorage]);

  // 3. Browser Back Button Trap & BeforeUnload Protection
  useEffect(() => {
    if (reviewMode || showResultModal) return;

    // Prevent accidental page refresh / close
    const handleBeforeUnload = (e) => {
      if (Object.keys(answers).length > 0) {
        saveProgressToStorage();
        e.preventDefault();
        e.returnValue = 'You have an exam in progress. Your answers have been saved.';
      }
    };
    window.addEventListener('beforeunload', handleBeforeUnload);

    // Prevent accidental browser Back button
    window.history.pushState(null, '', window.location.href);
    const handlePopState = () => {
      window.history.pushState(null, '', window.location.href);
      clearInterval(timerRef.current);
      setIsPaused(true);
      saveProgressToStorage();
      setShowExitModal(true);
    };
    window.addEventListener('popstate', handlePopState);

    return () => {
      window.removeEventListener('beforeunload', handleBeforeUnload);
      window.removeEventListener('popstate', handlePopState);
    };
  }, [reviewMode, showResultModal, answers, saveProgressToStorage]);

  // Format Timer mm:ss or hh:mm:ss
  const formatTime = (secs) => {
    const h = Math.floor(secs / 3600);
    const m = Math.floor((secs % 3600) / 60);
    const s = secs % 60;
    if (h > 0) {
      return `${h}:${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
    }
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  };

  // Pagination Math
  const totalPages = Math.max(1, Math.ceil(questions.length / QUESTIONS_PER_PAGE));
  const startIndex = (currentPage - 1) * QUESTIONS_PER_PAGE;
  const endIndex = Math.min(startIndex + QUESTIONS_PER_PAGE, questions.length);
  const pageQuestions = questions.slice(startIndex, endIndex);

  // Dynamic Section Ranges
  const sections = [];
  questions.forEach((q, idx) => {
    const qNum = q.qNumber || idx + 1;
    const secName = q.section || 'General Section';
    const existing = sections.find((s) => s.name === secName);
    if (!existing) {
      sections.push({
        name: secName,
        startQ: qNum,
        endQ: qNum,
        startPage: Math.floor((qNum - 1) / QUESTIONS_PER_PAGE) + 1,
      });
    } else {
      existing.endQ = qNum;
    }
  });

  // Track visited questions whenever page changes
  useEffect(() => {
    if (pageQuestions.length > 0) {
      setVisited((prev) => {
        const next = new Set(prev);
        pageQuestions.forEach((q) => next.add(q.qNumber || q.id));
        return next;
      });
    }
  }, [currentPage, questions]);

  // Handlers for Question Interactions
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

  // Jump to page
  const handleGoToPage = (pageNum) => {
    if (pageNum < 1 || pageNum > totalPages) return;
    setCurrentPage(pageNum);
    saveProgressToStorage(null, null, null, null, pageNum);
    if (typeof window !== 'undefined') {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  // Jump directly to a question (from palette or section pill)
  const handleJumpToQuestion = (qNum) => {
    const targetPage = Math.floor((qNum - 1) / QUESTIONS_PER_PAGE) + 1;
    setCurrentPage(targetPage);
    const updatedVisited = new Set(visited).add(qNum);
    setVisited(updatedVisited);
    saveProgressToStorage(null, null, updatedVisited, null, targetPage);
    setPaletteOpen(false);

    // Scroll to the specific question element and highlight it
    setTimeout(() => {
      const el = document.getElementById(`question-card-${qNum}`);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        setHighlightedQ(qNum);
        setTimeout(() => setHighlightedQ(null), 2500);
      }
    }, 150);
  };

  // Pause Test Handler
  const handlePauseTest = () => {
    clearInterval(timerRef.current);
    setIsPaused(true);
    saveProgressToStorage();
  };

  // Resume Test Handler
  const handleResumeTest = () => {
    setIsPaused(false);
    setShowExitModal(false);
  };

  // Exit Test Confirmation Trigger
  const handleAttemptExit = () => {
    if (reviewMode || showResultModal) {
      router.push('/dashboard');
      return;
    }
    clearInterval(timerRef.current);
    setIsPaused(true);
    saveProgressToStorage();
    setShowExitModal(true);
  };

  // Save & Confirm Exit to Dashboard
  const handleConfirmExit = () => {
    saveProgressToStorage();
    setShowExitModal(false);
    router.push('/dashboard');
  };

  // Discard & Quit
  const handleDiscardAndQuit = () => {
    clearSavedProgress();
    setShowExitModal(false);
    router.push('/dashboard');
  };

  // Restore saved attempt from resume prompt
  const handleAcceptResume = () => {
    if (resumePrompt) {
      setAnswers(resumePrompt.answers || {});
      setMarkedForReview(new Set(resumePrompt.markedForReview || []));
      setVisited(new Set(resumePrompt.visited || [1]));
      if (resumePrompt.timeLeft) setTimeLeft(resumePrompt.timeLeft);
      if (resumePrompt.currentPage) setCurrentPage(resumePrompt.currentPage);
      setResumePrompt(null);
      setIsPaused(false);
    }
  };

  // Reject resume and start fresh
  const handleRejectResume = () => {
    clearSavedProgress();
    setResumePrompt(null);
    setAnswers({});
    setMarkedForReview(new Set());
    const initialVisited = new Set();
    for (let i = 0; i < Math.min(10, questions.length); i++) {
      initialVisited.add(questions[i].qNumber || i + 1);
    }
    setVisited(initialVisited);
    setCurrentPage(1);
    setTimeLeft((testMeta?.durationMinutes || 180) * 60);
    startTimeRef.current = Date.now();
  };

  // 4. Submit Exam to Evaluation Engine
  const handleSubmitTest = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    clearInterval(timerRef.current);

    try {
      const durationSeconds = Math.round((Date.now() - startTimeRef.current) / 1000);
      const res = await fetch(`/api/tests/${testId}/submit`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          answers,
          startedAt: new Date(startTimeRef.current).toISOString(),
          durationSeconds,
        }),
      });

      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Evaluation failed');

      clearSavedProgress(); // Attempt successfully recorded; clear draft
      setResultData(data);
      setShowResultModal(true);

      try {
        confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
      } catch (e) {}
    } catch (err) {
      alert(`Submission error: ${err.message}`);
    } finally {
      setIsSubmitting(false);
    }
  };

  // Question Status Helper for Palette
  const getQuestionStatus = (qNum) => {
    const isAnswered = answers[qNum] !== undefined;
    const isMarked = markedForReview.has(qNum);
    const isVis = visited.has(qNum);

    if (isAnswered && isMarked) return 'answered_marked';
    if (isAnswered) return 'answered';
    if (isMarked) return 'marked';
    if (isVis) return 'not_answered';
    return 'not_visited';
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex flex-col items-center justify-center p-4 transition-colors">
        <div className="w-10 h-10 border-3 border-blue-600 border-t-transparent rounded-full animate-spin mb-4"></div>
        <h2 className="text-base font-bold text-slate-800 dark:text-slate-200">Preparing Test Paper...</h2>
        <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">Loading 10-questions-per-page navigation canvas</p>
      </div>
    );
  }

  // Paywall Gate Screen
  if (error?.isLocked) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex flex-col items-center justify-center p-4 transition-colors">
        <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-8 text-center shadow-lg">
          <div className="w-12 h-12 bg-amber-50 dark:bg-amber-950/50 text-amber-600 dark:text-amber-400 rounded-xl flex items-center justify-center mx-auto mb-4 border border-amber-200 dark:border-amber-800">
            <Lock className="w-6 h-6" />
          </div>
          <h1 className="text-xl font-bold text-slate-900 dark:text-white mb-2">Exam Locked</h1>
          <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
            This official 200-question test requires full access. Unlock all full-length papers, solutions, and analytics for just ₹99.
          </p>
          <div className="space-y-2.5">
            <Link
              href="/#pricing"
              className="block w-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100 font-bold py-3 rounded-xl transition-colors text-xs shadow-xs"
            >
              Unlock Full Access for ₹99
            </Link>
            <Link
              href="/exam/demo-test-50"
              className="block w-full bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 font-semibold py-2.5 rounded-xl transition-colors text-xs"
            >
              Take Free Demo Test Instead
            </Link>
          </div>
        </div>
      </div>
    );
  }

  if (error || questions.length === 0) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex flex-col items-center justify-center p-4 transition-colors">
        <AlertTriangle className="w-10 h-10 text-rose-500 mb-3" />
        <h2 className="text-base font-bold text-slate-800 dark:text-slate-200">Failed to Load Examination</h2>
        <p className="text-xs text-slate-500 dark:text-slate-400 mb-4">{error?.message || 'Question bank not available'}</p>
        <Link href="/dashboard" className="bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-semibold px-4 py-2 rounded-lg">
          Return to Dashboard
        </Link>
      </div>
    );
  }

  const answeredCount = Object.keys(answers).length;
  const markedCount = markedForReview.size;
  const reviewQuestionsList = resultData?.reviewQuestions || [];
  const filteredPaletteQuestions = questions.filter((q) => {
    if (paletteSectionFilter === 'all') return true;
    return (q.section || 'General Section') === paletteSectionFilter;
  });

  return (
    <div className="min-h-screen flex flex-col bg-slate-100 dark:bg-slate-950 text-slate-900 dark:text-slate-100 no-select pb-28 md:pb-24 transition-colors">
      
      {/* 1. STICKY TOP APP BAR (Responsive & Zero-Overflow on Mobile) */}
      <header className="sticky top-0 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white shadow-xs">
        <div className="max-w-[1440px] mx-auto px-2.5 sm:px-6 lg:px-8 h-13 sm:h-16 flex items-center justify-between gap-2">
          
          {/* Left: Safe Exit Button & Exam Title */}
          <div className="flex items-center gap-1.5 sm:gap-2.5 min-w-0">
            <button
              onClick={handleAttemptExit}
              type="button"
              className="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white p-1 rounded-lg cursor-pointer flex-shrink-0"
              title="Pause and Exit Test"
            >
              <ArrowLeft className="w-5 h-5" />
            </button>
            <div className="min-w-0">
              <div className="flex items-center gap-1.5">
                <span className="font-bold text-xs sm:text-sm text-slate-900 dark:text-white truncate">
                  {testMeta?.title || 'TSPLRB SI'}
                </span>
                <span className="hidden sm:inline-block bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-blue-200 dark:border-blue-800 flex-shrink-0">
                  Page {currentPage}/{totalPages} (Q{startIndex + 1}–{endIndex})
                </span>
              </div>
            </div>
          </div>

          {/* Center: Live Timer & Pause Button */}
          {!reviewMode && (
            <div className="flex items-center gap-1 sm:gap-1.5 flex-shrink-0">
              <div className={`flex items-center gap-1 px-2 sm:px-3 py-1 rounded-lg font-mono text-xs sm:text-sm font-bold border ${
                isPaused
                  ? 'bg-amber-50 dark:bg-amber-950/60 border-amber-300 dark:border-amber-700 text-amber-700 dark:text-amber-300'
                  : timeLeft < 600
                  ? 'bg-rose-50 dark:bg-rose-950/80 border-rose-200 dark:border-rose-800 text-rose-600 dark:text-rose-300 animate-pulse'
                  : 'bg-slate-50 dark:bg-slate-950 border-slate-200 dark:border-slate-800 text-slate-800 dark:text-amber-400'
              }`}>
                <Clock className="w-3.5 h-3.5 text-blue-600 dark:text-amber-400" />
                <span>{isPaused ? 'PAUSED' : formatTime(timeLeft)}</span>
              </div>

              {/* Pause / Resume Button */}
              <button
                onClick={isPaused ? handleResumeTest : handlePauseTest}
                type="button"
                className={`p-1 sm:px-2 sm:py-1 rounded-lg border text-xs font-semibold flex items-center gap-1 transition-colors cursor-pointer shadow-xs ${
                  isPaused
                    ? 'bg-emerald-600 text-white border-emerald-600 hover:bg-emerald-700'
                    : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-200 dark:border-slate-700 hover:bg-slate-50'
                }`}
                title={isPaused ? 'Resume exam' : 'Pause exam and save answers'}
              >
                {isPaused ? <Play className="w-3.5 h-3.5 fill-current" /> : <Pause className="w-3.5 h-3.5 fill-current" />}
                <span className="hidden md:inline">{isPaused ? 'Resume' : 'Pause'}</span>
              </button>
            </div>
          )}

          {/* Right: Language (Desktop), Theme & Palette Toggle */}
          <div className="flex items-center gap-1.5 sm:gap-2 flex-shrink-0">
            
            {/* Desktop Language Mode Toggle */}
            <div className="hidden md:flex items-center bg-slate-100 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-lg p-0.5 text-[10px] font-bold">
              <button
                onClick={() => setLangMode('dual')}
                className={`px-2 py-0.5 rounded cursor-pointer ${langMode === 'dual' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs' : 'text-slate-500 dark:text-slate-400'}`}
              >
                Dual
              </button>
              <button
                onClick={() => setLangMode('en')}
                className={`px-2 py-0.5 rounded cursor-pointer ${langMode === 'en' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs' : 'text-slate-500 dark:text-slate-400'}`}
              >
                EN
              </button>
              <button
                onClick={() => setLangMode('te')}
                className={`px-2 py-0.5 rounded cursor-pointer ${langMode === 'te' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs' : 'text-slate-500 dark:text-slate-400'}`}
              >
                తెలుగు
              </button>
            </div>

            <ThemeToggle />

            {/* Questions Palette Toggle Button (Always visible on mobile & desktop) */}
            <button
              onClick={() => setPaletteOpen(true)}
              className="bg-blue-600 hover:bg-blue-700 text-white px-2.5 py-1.5 rounded-lg flex items-center gap-1 text-xs font-bold shadow-xs cursor-pointer"
              title="Open questions palette"
            >
              <Menu className="w-3.5 h-3.5" />
              <span>Palette</span>
              <span className="bg-white/20 text-[10px] px-1 rounded-full">
                {answeredCount}
              </span>
            </button>

          </div>

        </div>
      </header>

      {/* 2. SECTION & PAGE QUICK JUMP NAVIGATOR */}
      <div className="sticky top-13 sm:top-16 z-20 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 py-2 px-2.5 sm:px-6 lg:px-8 shadow-xs">
        <div className="max-w-[1440px] mx-auto flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2">
          
          {/* Section Quick Jump Buttons + Mobile Language Toggle */}
          <div className="flex items-center gap-1.5 overflow-x-auto w-full sm:w-auto pb-1 sm:pb-0 scrollbar-none">
            
            {/* Mobile-only Language Selector */}
            <div className="md:hidden flex items-center bg-slate-100 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-lg p-0.5 text-[10px] font-bold flex-shrink-0 mr-1">
              <button
                onClick={() => setLangMode('dual')}
                className={`px-1.5 py-0.5 rounded ${langMode === 'dual' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white' : 'text-slate-500'}`}
              >
                Dual
              </button>
              <button
                onClick={() => setLangMode('en')}
                className={`px-1.5 py-0.5 rounded ${langMode === 'en' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white' : 'text-slate-500'}`}
              >
                EN
              </button>
              <button
                onClick={() => setLangMode('te')}
                className={`px-1.5 py-0.5 rounded ${langMode === 'te' ? 'bg-white dark:bg-slate-800 text-slate-900 dark:text-white' : 'text-slate-500'}`}
              >
                తె
              </button>
            </div>

            <span className="text-[11px] font-semibold text-slate-500 dark:text-slate-400 flex items-center gap-1 flex-shrink-0 mr-1">
              <Layers className="w-3.5 h-3.5" />
              <span>Sections:</span>
            </span>
            {sections.map((sec, idx) => {
              const isSecActive = currentPage >= sec.startPage && currentPage <= Math.floor((sec.endQ - 1) / QUESTIONS_PER_PAGE) + 1;
              return (
                <button
                  key={idx}
                  onClick={() => handleGoToPage(sec.startPage)}
                  className={`text-xs px-2.5 py-1 rounded-lg border font-medium flex-shrink-0 transition-colors cursor-pointer ${
                    isSecActive
                      ? 'bg-blue-600 text-white border-blue-600 shadow-xs'
                      : 'bg-slate-50 dark:bg-slate-800/80 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-100'
                  }`}
                >
                  <span>{sec.name}</span>
                  <span className="ml-1 opacity-80 text-[10px]">({sec.startQ}–{sec.endQ})</span>
                </button>
              );
            })}
          </div>

          {/* Page Jump Pills (1-10, 11-20, ...) */}
          <div className="flex items-center gap-1.5 overflow-x-auto w-full sm:w-auto pb-1 sm:pb-0 scrollbar-none">
            <span className="text-[11px] font-semibold text-slate-500 dark:text-slate-400 flex-shrink-0 mr-1">
              Page:
            </span>
            <div className="flex items-center gap-1">
              {Array.from({ length: totalPages }).map((_, pIdx) => {
                const pageNum = pIdx + 1;
                const pStartQ = (pageNum - 1) * QUESTIONS_PER_PAGE + 1;
                const pEndQ = Math.min(pageNum * QUESTIONS_PER_PAGE, questions.length);
                const isCurrent = currentPage === pageNum;

                // Check how many answered on this page
                let pageAnsweredCount = 0;
                for (let q = pStartQ; q <= pEndQ; q++) {
                  if (answers[q] !== undefined) pageAnsweredCount++;
                }

                return (
                  <button
                    key={pageNum}
                    onClick={() => handleGoToPage(pageNum)}
                    className={`text-xs px-2 py-1 rounded-md border font-semibold flex-shrink-0 transition-all cursor-pointer ${
                      isCurrent
                        ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 border-slate-900 dark:border-white shadow-xs'
                        : pageAnsweredCount === (pEndQ - pStartQ + 1)
                        ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300'
                        : 'bg-white dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-400 hover:bg-slate-50'
                    }`}
                    title={`Questions ${pStartQ} to ${pEndQ} (${pageAnsweredCount}/${pEndQ - pStartQ + 1} answered)`}
                  >
                    <span>P{pageNum}</span>
                    <span className="text-[10px] ml-0.5 opacity-70">({pStartQ}–{pEndQ})</span>
                  </button>
                );
              })}
            </div>
          </div>

        </div>
      </div>

      {/* 3. MAIN EXAM BODY (10 QUESTIONS PER PAGE) */}
      <div className="flex-1 max-w-[1440px] w-full mx-auto px-2 sm:px-6 lg:px-8 flex flex-col lg:flex-row">
        
        {/* Left: The 10 Questions Stream */}
        <main className="flex-1 p-3 sm:p-6 overflow-y-auto space-y-6" ref={mainContentRef}>
          
          {/* Pause Banner (If Paused) */}
          {isPaused && (
            <div className="bg-amber-50 dark:bg-amber-950/50 border border-amber-300 dark:border-amber-800 rounded-xl p-4 flex flex-col sm:flex-row items-center justify-between gap-3 shadow-xs">
              <div className="flex items-center gap-2.5 text-xs text-amber-900 dark:text-amber-200">
                <Pause className="w-5 h-5 text-amber-600 dark:text-amber-400 flex-shrink-0" />
                <div>
                  <div className="font-bold">Examination is Paused</div>
                  <div className="text-[11px] opacity-90">Timer is paused. All your responses are automatically saved.</div>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <button
                  onClick={handleResumeTest}
                  className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-4 py-1.5 rounded-lg text-xs shadow-xs flex items-center gap-1 cursor-pointer"
                >
                  <Play className="w-3.5 h-3.5 fill-current" />
                  <span>Resume Test</span>
                </button>
                <button
                  onClick={handleConfirmExit}
                  className="bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 border border-slate-200 dark:border-slate-700 px-3 py-1.5 rounded-lg text-xs font-semibold hover:bg-slate-50 cursor-pointer"
                >
                  Save & Exit
                </button>
              </div>
            </div>
          )}

          {/* Page Banner */}
          <div className="flex items-center justify-between bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl px-4 py-3 shadow-xs">
            <div className="flex items-center gap-2">
              <span className="font-bold text-sm text-slate-900 dark:text-white">
                Questions {startIndex + 1} to {endIndex} of {questions.length}
              </span>
              <span className="text-xs text-slate-500 dark:text-slate-400">
                • Page {currentPage} of {totalPages}
              </span>
            </div>
            
            <div className="flex items-center gap-1.5">
              <button
                onClick={() => handleGoToPage(currentPage - 1)}
                disabled={currentPage === 1}
                className="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer"
                title="Previous 10 Questions"
              >
                <ChevronLeft className="w-4 h-4" />
              </button>
              <button
                onClick={() => handleGoToPage(currentPage + 1)}
                disabled={currentPage === totalPages}
                className="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer"
                title="Next 10 Questions"
              >
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Render 10 Question Cards */}
          {pageQuestions.map((q, qIndexOnPage) => {
            const qNum = q.qNumber || startIndex + qIndexOnPage + 1;
            const isSelected = answers[qNum] !== undefined;
            const isMarked = markedForReview.has(qNum);
            const isHighlighted = highlightedQ === qNum;

            // Review mode data
            const qRev = reviewMode && resultData ? reviewQuestionsList.find((r) => r.qNumber === qNum) : null;

            return (
              <article
                key={qNum}
                id={`question-card-${qNum}`}
                className={`bg-white dark:bg-slate-900 border rounded-xl sm:rounded-2xl p-4 sm:p-7 shadow-xs transition-all duration-300 ${
                  isHighlighted
                    ? 'ring-3 ring-blue-600 dark:ring-amber-400 border-blue-600 dark:border-amber-400'
                    : isMarked
                    ? 'border-purple-300 dark:border-purple-800 bg-purple-50/15 dark:bg-purple-950/10'
                    : isSelected
                    ? 'border-slate-300 dark:border-slate-700'
                    : 'border-slate-200 dark:border-slate-800'
                }`}
              >
                {/* Question Header & Quick Actions */}
                <div className="flex items-center justify-between pb-3 mb-4 border-b border-slate-100 dark:border-slate-800 text-xs">
                  <div className="flex items-center gap-2">
                    <span className="font-bold text-xs px-2.5 py-0.5 rounded-md bg-slate-900 dark:bg-white text-white dark:text-slate-950">
                      Q {qNum}
                    </span>
                    <span className="font-semibold text-blue-600 dark:text-amber-400">
                      {q.section}
                    </span>
                    {q.topic && (
                      <span className="text-[11px] text-slate-500 dark:text-slate-400 hidden sm:inline">
                        • {q.topic}
                      </span>
                    )}
                  </div>

                  <div className="flex items-center gap-2">
                    {/* Mark for review button */}
                    {!reviewMode && (
                      <button
                        onClick={() => handleToggleReview(qNum)}
                        className={`px-2.5 py-1 rounded-md text-[11px] font-semibold border transition-colors flex items-center gap-1 cursor-pointer ${
                          isMarked
                            ? 'bg-purple-600 text-white border-purple-600'
                            : 'bg-slate-50 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-100'
                        }`}
                        title="Mark this question to review later"
                      >
                        <Bookmark className="w-3 h-3" />
                        <span className="hidden sm:inline">{isMarked ? 'Marked' : 'Review'}</span>
                      </button>
                    )}

                    {/* Clear selection button */}
                    {!reviewMode && isSelected && (
                      <button
                        onClick={() => handleClearAnswer(qNum)}
                        className="px-2 py-1 bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700 text-slate-500 dark:text-slate-400 rounded-md text-[11px] font-medium cursor-pointer"
                        title="Clear selected option"
                      >
                        Clear
                      </button>
                    )}

                    <span className="text-[11px] text-slate-400 pl-1 border-l border-slate-200 dark:border-slate-800">
                      +1.0 / -0.20
                    </span>
                  </div>
                </div>

                {/* Question Statement (Bilingual) */}
                <div className="space-y-3 mb-6">
                  {(langMode === 'dual' || langMode === 'en') && (
                    <div className="text-sm sm:text-base font-semibold text-slate-900 dark:text-white leading-relaxed">
                      {q.question_en}
                    </div>
                  )}

                  {(langMode === 'dual' || langMode === 'te') && (
                    <div className="text-sm sm:text-base font-medium text-slate-700 dark:text-amber-200/90 leading-relaxed font-sans border-t border-slate-100 dark:border-slate-800/60 pt-2.5">
                      {q.question_te}
                    </div>
                  )}
                </div>

                {/* 4 Options Grid */}
                <div className="space-y-2.5">
                  {q.options_en.map((optEn, optIdx) => {
                    const optTe = q.options_te?.[optIdx] || '';
                    const isOptionChosen = answers[qNum] === optIdx;

                    // Review mode color decoration
                    let reviewStyle = '';
                    if (reviewMode && qRev) {
                      if (optIdx === qRev.correct_option) {
                        reviewStyle = 'border-emerald-500 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-950 dark:text-emerald-200 font-medium';
                      } else if (isOptionChosen && !qRev.isCorrect) {
                        reviewStyle = 'border-rose-500 bg-rose-50 dark:bg-rose-950/60 text-rose-950 dark:text-rose-200';
                      }
                    }

                    return (
                      <button
                        key={optIdx}
                        onClick={() => handleSelectOption(qNum, optIdx)}
                        disabled={reviewMode}
                        className={`w-full text-left p-3 sm:p-3.5 rounded-xl border transition-all flex items-start gap-3 cursor-pointer ${
                          reviewStyle
                            ? reviewStyle
                            : isOptionChosen
                            ? 'border-blue-600 bg-blue-50 dark:bg-blue-950/60 text-blue-950 dark:text-white shadow-xs'
                            : 'border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/60 hover:bg-slate-100 dark:hover:bg-slate-800/60 text-slate-800 dark:text-slate-200'
                        }`}
                      >
                        {/* Option Radio Letter (A, B, C, D) */}
                        <div
                          className={`w-6 h-6 rounded-full flex-shrink-0 flex items-center justify-center font-bold text-xs mt-0.5 border ${
                            isOptionChosen
                              ? 'border-blue-600 bg-blue-600 text-white'
                              : 'border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                          }`}
                        >
                          {String.fromCharCode(65 + optIdx)}
                        </div>

                        {/* Option Text */}
                        <div className="flex-1 space-y-0.5">
                          {(langMode === 'dual' || langMode === 'en') && (
                            <div className="text-xs sm:text-sm font-medium">{optEn}</div>
                          )}
                          {(langMode === 'dual' || langMode === 'te') && optTe && (
                            <div className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 font-sans">{optTe}</div>
                          )}
                        </div>

                        {/* Answer indicator in review mode */}
                        {reviewMode && qRev && optIdx === qRev.correct_option && (
                          <span className="text-[11px] font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-100 dark:bg-emerald-950/80 px-2 py-0.5 rounded-md flex-shrink-0">
                            Correct Answer
                          </span>
                        )}
                      </button>
                    );
                  })}
                </div>

                {/* Explanation Box in Review Mode */}
                {reviewMode && qRev && (
                  <div className="mt-5 p-4 bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl space-y-2.5">
                    <div className="flex items-center gap-1.5 text-xs font-bold text-slate-900 dark:text-amber-400">
                      <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                      <span>Official Solution & Explanation</span>
                    </div>
                    <div className="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed">
                      <strong className="text-slate-900 dark:text-slate-100">English: </strong>
                      {qRev.explanation_en}
                    </div>
                    <div className="text-xs sm:text-sm text-slate-700 dark:text-amber-200/90 leading-relaxed font-sans">
                      <strong className="text-slate-900 dark:text-amber-300">తెలుగు వివరణ: </strong>
                      {qRev.explanation_te}
                    </div>
                  </div>
                )}
              </article>
            );
          })}

          {/* Bottom Pagination Controls at the end of the 10 questions */}
          <div className="flex items-center justify-between pt-4 pb-12">
            <button
              onClick={() => handleGoToPage(currentPage - 1)}
              disabled={currentPage === 1}
              className="px-4 py-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-800 disabled:opacity-40 disabled:cursor-not-allowed flex items-center gap-1 shadow-xs cursor-pointer"
            >
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>Previous 10 Questions</span>
            </button>

            <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">
              Page {currentPage} of {totalPages}
            </span>

            {currentPage < totalPages ? (
              <button
                onClick={() => handleGoToPage(currentPage + 1)}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-xs font-bold flex items-center gap-1 shadow-xs cursor-pointer"
              >
                <span>Next 10 Questions</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            ) : (
              !reviewMode && (
                <button
                  onClick={handleSubmitTest}
                  disabled={isSubmitting}
                  className="px-5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-xs cursor-pointer"
                >
                  {isSubmitting ? 'Evaluating...' : 'Submit Test'}
                </button>
              )
            )}
          </div>

        </main>

        {/* Right: Desktop Sidebar Questions Palette (Pinned Sticky on UI Screen) */}
        <aside className="hidden lg:flex flex-col w-80 p-5 border-l border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 sticky top-[116px] h-[calc(100vh-176px)] self-start shadow-xs">
          <div className="flex items-center justify-between mb-3 flex-shrink-0">
            <div className="flex items-center gap-1.5">
              <LayoutGrid className="w-4 h-4 text-blue-600 dark:text-amber-400" />
              <h3 className="font-bold text-sm text-slate-900 dark:text-white">Questions Palette</h3>
            </div>
            <span className="text-[11px] text-slate-500 font-medium">
              {answeredCount}/{questions.length} Answered
            </span>
          </div>
          
          {/* Legend */}
          <div className="grid grid-cols-2 gap-2 text-[10px] text-slate-500 dark:text-slate-400 mb-3 pb-3 border-b border-slate-100 dark:border-slate-800 flex-shrink-0">
            <div className="flex items-center gap-1.5">
              <span className="w-2.5 h-2.5 rounded-full bg-emerald-600"></span> Answered ({answeredCount})
            </div>
            <div className="flex items-center gap-1.5">
              <span className="w-2.5 h-2.5 rounded-full bg-rose-600"></span> Not Answered
            </div>
            <div className="flex items-center gap-1.5">
              <span className="w-2.5 h-2.5 rounded-full bg-purple-600"></span> Review ({markedCount})
            </div>
            <div className="flex items-center gap-1.5">
              <span className="w-2.5 h-2.5 rounded-full bg-slate-200 dark:bg-slate-800 border border-slate-300 dark:border-slate-700"></span> Unvisited
            </div>
          </div>

          {/* 1-200 Questions Grid (Scrolls internally within the sticky palette) */}
          <div className="grid grid-cols-5 gap-1.5 overflow-y-auto pr-1 flex-1 min-h-0">
            {questions.map((q, idx) => {
              const qNum = q.qNumber || idx + 1;
              const status = getQuestionStatus(qNum);
              const isCurrentPageQ = qNum >= startIndex + 1 && qNum <= endIndex;

              let colorClasses = 'bg-slate-50 dark:bg-slate-950 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-800';
              if (status === 'answered') colorClasses = 'bg-emerald-600 text-white border-emerald-600 shadow-xs';
              else if (status === 'not_answered') colorClasses = 'bg-rose-600 text-white border-rose-600 shadow-xs';
              else if (status === 'marked' || status === 'answered_marked') colorClasses = 'bg-purple-600 text-white border-purple-600 shadow-xs';

              return (
                <button
                  key={qNum}
                  onClick={() => handleJumpToQuestion(qNum)}
                  className={`h-8 rounded-lg font-bold text-xs flex items-center justify-center border transition-all cursor-pointer ${colorClasses} ${
                    isCurrentPageQ ? 'ring-2 ring-blue-600/80 dark:ring-amber-400/80 ring-offset-1' : ''
                  }`}
                  title={`Jump to Question ${qNum}`}
                >
                  {qNum}
                </button>
              );
            })}
          </div>

          {/* Submit Examination Button (Docked at bottom of sticky aside) */}
          {!reviewMode && (
            <button
              onClick={handleSubmitTest}
              disabled={isSubmitting}
              className="w-full mt-4 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 rounded-xl transition-all shadow-xs text-xs cursor-pointer flex-shrink-0"
            >
              {isSubmitting ? 'Evaluating Test...' : 'Submit & Finish Examination'}
            </button>
          )}
        </aside>

      </div>

      {/* 4. FIXED BOTTOM STATUS & CONTROLS BAR */}
      <footer className="fixed bottom-0 left-0 right-0 z-30 bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 p-2 sm:p-3 shadow-md">
        <div className="max-w-[1440px] mx-auto px-2.5 sm:px-6 lg:px-8 flex items-center justify-between gap-2">
          
          {/* Progress summary */}
          <div className="flex items-center gap-2 sm:gap-3 text-xs">
            <span className="font-bold text-slate-900 dark:text-white">
              Page {currentPage}/{totalPages}
            </span>
            <span className="hidden sm:inline text-slate-500 dark:text-slate-400">
              • Ans: <strong className="text-emerald-600 dark:text-emerald-400">{answeredCount}</strong>/{questions.length}
            </span>
            {markedCount > 0 && (
              <span className="hidden sm:inline text-purple-600 dark:text-purple-400 font-semibold">
                • Marked: {markedCount}
              </span>
            )}
          </div>

          {/* Mobile Bottom Bar Trigger: Questions Palette Button */}
          <button
            onClick={() => setPaletteOpen(true)}
            type="button"
            className="lg:hidden flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-blue-50 dark:bg-blue-950/60 border border-blue-200 dark:border-blue-800 text-blue-700 dark:text-blue-300 font-bold text-xs hover:bg-blue-100 dark:hover:bg-blue-900 cursor-pointer shadow-xs"
            title="Open 200 Questions Palette"
          >
            <LayoutGrid className="w-3.5 h-3.5" />
            <span>Palette ({answeredCount})</span>
          </button>

          {/* Prev / Next 10 buttons */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            <button
              onClick={() => handleGoToPage(currentPage - 1)}
              disabled={currentPage === 1}
              className="px-2.5 sm:px-4 py-1.5 sm:py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 disabled:opacity-40 text-slate-700 dark:text-slate-200 rounded-lg text-xs font-bold border border-slate-200 dark:border-slate-700 flex items-center gap-1 cursor-pointer"
            >
              <ArrowLeft className="w-3.5 h-3.5" />
              <span>Prev 10</span>
            </button>

            {currentPage < totalPages ? (
              <button
                onClick={() => handleGoToPage(currentPage + 1)}
                className="px-3 sm:px-5 py-1.5 sm:py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-bold flex items-center gap-1 shadow-xs cursor-pointer"
              >
                <span>Next 10</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            ) : (
              !reviewMode && (
                <button
                  onClick={handleSubmitTest}
                  disabled={isSubmitting}
                  className="px-3 sm:px-5 py-1.5 sm:py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold shadow-xs cursor-pointer"
                >
                  {isSubmitting ? 'Evaluating...' : 'Submit Test'}
                </button>
              )
            )}
          </div>

        </div>
      </footer>

      {/* 5. FLOATING QUICK-PALETTE PILL (Visible on Mobile & Tall Viewports < lg) */}
      <div className="fixed bottom-16 sm:bottom-20 right-3 sm:right-6 z-40 lg:hidden">
        <button
          onClick={() => setPaletteOpen(true)}
          type="button"
          className="flex items-center gap-2 px-3.5 py-2.5 rounded-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 shadow-2xl active:scale-95 border border-slate-700 dark:border-slate-200 font-bold text-xs transition-all cursor-pointer"
          title="Open questions palette"
        >
          <LayoutGrid className="w-4 h-4 text-blue-400 dark:text-blue-600" />
          <span>Questions</span>
          <span className="bg-blue-600 dark:bg-blue-600 text-white text-[10px] px-1.5 py-0.5 rounded-full font-mono">
            {answeredCount}/{questions.length}
          </span>
        </button>
      </div>

      {/* 6. MOBILE & TALL ASPECT RATIO QUESTION PALETTE DRAWER (Full-height h-[100dvh]) */}
      {paletteOpen && (
        <div className="fixed inset-0 z-50 flex justify-end">
          {/* Backdrop */}
          <div
            onClick={() => setPaletteOpen(false)}
            className="fixed inset-0 bg-slate-950/60 backdrop-blur-xs transition-opacity"
          />

          {/* Slide-over Drawer (h-[100dvh] guarantees full-screen coverage on all mobile devices & tall screens) */}
          <div className="relative w-full max-w-sm sm:max-w-md bg-white dark:bg-slate-900 border-l border-slate-200 dark:border-slate-800 flex flex-col h-[100dvh] max-h-screen shadow-2xl z-10">
            
            {/* Header (Pinned at top) */}
            <div className="p-4 sm:p-5 border-b border-slate-200 dark:border-slate-800 flex-shrink-0">
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-2">
                  <LayoutGrid className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                  <h3 className="font-bold text-sm sm:text-base text-slate-900 dark:text-white">Questions Palette</h3>
                  <span className="bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 text-xs font-bold px-2 py-0.5 rounded-full border border-blue-200 dark:border-blue-800">
                    {answeredCount}/{questions.length}
                  </span>
                </div>
                <button
                  onClick={() => setPaletteOpen(false)}
                  className="text-slate-400 hover:text-slate-700 dark:hover:text-white p-1 rounded-lg cursor-pointer"
                  title="Close palette"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Legend */}
              <div className="grid grid-cols-2 gap-2 text-[10px] text-slate-500 dark:text-slate-400 pb-3 border-b border-slate-100 dark:border-slate-800">
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-emerald-600"></span> Answered ({answeredCount})
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-rose-600"></span> Not Answered
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-purple-600"></span> Marked ({markedCount})
                </div>
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full bg-slate-200 dark:bg-slate-800 border border-slate-300 dark:border-slate-700"></span> Unvisited
                </div>
              </div>

              {/* Section Filters (Quick Filter by Section) */}
              <div className="flex items-center gap-1.5 pt-2.5 overflow-x-auto scrollbar-none">
                <button
                  onClick={() => setPaletteSectionFilter('all')}
                  className={`text-[11px] px-2.5 py-1 rounded-md font-bold transition-colors cursor-pointer flex-shrink-0 ${
                    paletteSectionFilter === 'all'
                      ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 shadow-xs'
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                  }`}
                >
                  All ({questions.length})
                </button>
                {sections.map((sec, idx) => (
                  <button
                    key={idx}
                    onClick={() => setPaletteSectionFilter(sec.name)}
                    className={`text-[11px] px-2.5 py-1 rounded-md font-bold transition-colors cursor-pointer flex-shrink-0 ${
                      paletteSectionFilter === sec.name
                        ? 'bg-blue-600 text-white shadow-xs'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 hover:bg-slate-200 dark:hover:bg-slate-700'
                    }`}
                  >
                    <span>{sec.name}</span>
                    <span className="ml-1 opacity-75 text-[10px]">({sec.startQ}–{sec.endQ})</span>
                  </button>
                ))}
              </div>
            </div>

            {/* Scrollable Questions Grid (Fills remaining height smoothly) */}
            <div className="flex-1 overflow-y-auto p-4 sm:p-5 min-h-0">
              <div className="grid grid-cols-5 sm:grid-cols-6 gap-2">
                {filteredPaletteQuestions.map((q, idx) => {
                  const qNum = q.qNumber || idx + 1;
                  const status = getQuestionStatus(qNum);
                  const isCurrentPageQ = qNum >= startIndex + 1 && qNum <= endIndex;

                  let colorClasses = 'bg-slate-50 dark:bg-slate-950 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-800';
                  if (status === 'answered') colorClasses = 'bg-emerald-600 text-white border-emerald-600 shadow-xs';
                  else if (status === 'not_answered') colorClasses = 'bg-rose-600 text-white border-rose-600 shadow-xs';
                  else if (status === 'marked' || status === 'answered_marked') colorClasses = 'bg-purple-600 text-white border-purple-600 shadow-xs';

                  return (
                    <button
                      key={qNum}
                      onClick={() => handleJumpToQuestion(qNum)}
                      className={`h-9 rounded-lg font-bold text-xs flex items-center justify-center border transition-all cursor-pointer ${colorClasses} ${
                        isCurrentPageQ ? 'ring-2 ring-blue-600 dark:ring-amber-400 ring-offset-1' : ''
                      }`}
                      title={`Jump to Question ${qNum}`}
                    >
                      {qNum}
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Pinned Footer (Docked at bottom of drawer) */}
            <div className="p-4 sm:p-5 border-t border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 flex-shrink-0 space-y-2">
              {!reviewMode ? (
                <button
                  onClick={() => {
                    setPaletteOpen(false);
                    handleSubmitTest();
                  }}
                  disabled={isSubmitting}
                  className="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 rounded-xl text-xs transition-colors shadow-xs cursor-pointer flex items-center justify-center gap-1.5"
                >
                  <CheckCircle2 className="w-4 h-4" />
                  <span>{isSubmitting ? 'Evaluating Test...' : 'Submit & Finish Examination'}</span>
                </button>
              ) : (
                <button
                  onClick={() => setPaletteOpen(false)}
                  className="w-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-bold py-2.5 rounded-xl text-xs transition-colors shadow-xs cursor-pointer"
                >
                  Close Palette
                </button>
              )}
            </div>

          </div>
        </div>
      )}

      {/* 6. EXIT / PAUSE CONFIRMATION MODAL */}
      {showExitModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-xs">
          <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-7 shadow-2xl relative">
            
            <div className="w-12 h-12 bg-amber-50 dark:bg-amber-950/40 text-amber-600 dark:text-amber-400 rounded-xl flex items-center justify-center mx-auto mb-4 border border-amber-200 dark:border-amber-800 shadow-xs">
              <Pause className="w-6 h-6 fill-current" />
            </div>

            <h2 className="text-lg font-bold text-slate-900 dark:text-white text-center">Pause & Exit Examination?</h2>
            <p className="text-xs text-slate-600 dark:text-slate-400 text-center mt-1 mb-5 leading-relaxed">
              You have an active exam in progress. Your answers and remaining time will be saved automatically so you can resume anytime.
            </p>

            {/* Current Session Summary */}
            <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl p-3.5 mb-5 grid grid-cols-3 gap-2 text-center text-xs">
              <div>
                <div className="text-slate-400 text-[10px]">Answered</div>
                <div className="font-bold text-emerald-600 dark:text-emerald-400 text-sm mt-0.5">{answeredCount}/{questions.length}</div>
              </div>
              <div>
                <div className="text-slate-400 text-[10px]">Time Left</div>
                <div className="font-bold text-slate-900 dark:text-white text-sm mt-0.5">{formatTime(timeLeft)}</div>
              </div>
              <div>
                <div className="text-slate-400 text-[10px]">Current Page</div>
                <div className="font-bold text-blue-600 dark:text-blue-400 text-sm mt-0.5">P{currentPage}/{totalPages}</div>
              </div>
            </div>

            <div className="space-y-2.5">
              <button
                onClick={handleResumeTest}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl text-xs transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Continue Taking Exam</span>
              </button>

              <button
                onClick={handleConfirmExit}
                className="w-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100 font-bold py-2.5 rounded-xl text-xs transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <Save className="w-3.5 h-3.5" />
                <span>Save Progress & Exit to Dashboard</span>
              </button>

              <button
                onClick={handleDiscardAndQuit}
                className="w-full text-rose-600 dark:text-rose-400 hover:text-rose-700 text-[11px] font-medium py-1 text-center transition-colors cursor-pointer"
              >
                Discard attempt and start fresh next time
              </button>
            </div>

          </div>
        </div>
      )}

      {/* 7. RESUME PREVIOUS ATTEMPT PROMPT (Shown on fresh visit if saved progress exists) */}
      {resumePrompt && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-xs">
          <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-7 shadow-2xl relative">
            
            <div className="w-12 h-12 bg-blue-50 dark:bg-blue-950/40 text-blue-600 dark:text-blue-400 rounded-xl flex items-center justify-center mx-auto mb-4 border border-blue-200 dark:border-blue-800 shadow-xs">
              <RotateCcw className="w-6 h-6" />
            </div>

            <h2 className="text-lg font-bold text-slate-900 dark:text-white text-center">Resume Previous Attempt?</h2>
            <p className="text-xs text-slate-600 dark:text-slate-400 text-center mt-1 mb-5 leading-relaxed">
              We found an unfinished exam session saved on this device. Would you like to resume where you left off?
            </p>

            {/* Saved Attempt Stats */}
            <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl p-3.5 mb-5 grid grid-cols-3 gap-2 text-center text-xs">
              <div>
                <div className="text-slate-400 text-[10px]">Saved Answers</div>
                <div className="font-bold text-emerald-600 dark:text-emerald-400 text-sm mt-0.5">
                  {Object.keys(resumePrompt.answers || {}).length}/{questions.length}
                </div>
              </div>
              <div>
                <div className="text-slate-400 text-[10px]">Time Left</div>
                <div className="font-bold text-slate-900 dark:text-white text-sm mt-0.5">
                  {formatTime(resumePrompt.timeLeft || 180 * 60)}
                </div>
              </div>
              <div>
                <div className="text-slate-400 text-[10px]">Saved Page</div>
                <div className="font-bold text-blue-600 dark:text-blue-400 text-sm mt-0.5">
                  P{resumePrompt.currentPage || 1}
                </div>
              </div>
            </div>

            <div className="space-y-2.5">
              <button
                onClick={handleAcceptResume}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl text-xs transition-colors shadow-xs flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Resume Previous Attempt</span>
              </button>

              <button
                onClick={handleRejectResume}
                className="w-full bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 font-semibold py-2.5 rounded-xl text-xs transition-colors cursor-pointer"
              >
                <span>Start Fresh Attempt (Reset Answers)</span>
              </button>
            </div>

          </div>
        </div>
      )}

      {/* 8. SCORECARD & EVALUATION MODAL */}
      {showResultModal && resultData && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-xs overflow-y-auto">
          <div className="max-w-lg w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-8 shadow-2xl relative my-8">
            
            <div className="text-center mb-6">
              <div className="w-12 h-12 bg-amber-50 dark:bg-amber-950/50 text-amber-600 dark:text-amber-400 rounded-xl flex items-center justify-center mx-auto mb-2 border border-amber-200 dark:border-amber-800">
                <Trophy className="w-6 h-6" />
              </div>
              <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">Exam Completed</h2>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">Official TSPLRB SI Prelims Evaluation (-0.20 Negative Marking Applied)</p>
            </div>

            {/* Scorecard Hero */}
            <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl p-5 text-center mb-6">
              <div className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Your Final Score</div>
              <div className="text-4xl sm:text-5xl font-black text-slate-900 dark:text-white mt-1">
                {resultData.totalScore}
                <span className="text-base sm:text-lg text-slate-400 font-normal"> / {resultData.totalMarks}</span>
              </div>
              <div className="text-xs text-emerald-600 dark:text-emerald-400 font-bold mt-2">
                Accuracy: {resultData.accuracyPercent}%
              </div>
            </div>

            {/* Performance Stats Grid */}
            <div className="grid grid-cols-3 gap-2.5 mb-6 text-center text-xs">
              <div className="bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800 rounded-lg p-3">
                <div className="text-emerald-700 dark:text-emerald-400 font-bold text-lg">{resultData.correctCount}</div>
                <div className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Correct (+1)</div>
              </div>
              <div className="bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800 rounded-lg p-3">
                <div className="text-rose-700 dark:text-rose-400 font-bold text-lg">{resultData.wrongCount}</div>
                <div className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Wrong (-0.20)</div>
              </div>
              <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-lg p-3">
                <div className="text-slate-700 dark:text-slate-300 font-bold text-lg">{resultData.unansweredCount}</div>
                <div className="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Unanswered</div>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="space-y-2.5">
              <button
                onClick={() => {
                  setShowResultModal(false);
                  setReviewMode(true);
                  setCurrentPage(1);
                }}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl text-xs sm:text-sm transition-colors shadow-xs flex items-center justify-center gap-2 cursor-pointer"
              >
                <span>Review Question-by-Question Solutions</span>
              </button>

              <div className="grid grid-cols-2 gap-2">
                <button
                  onClick={() => {
                    clearSavedProgress();
                    setAnswers({});
                    setMarkedForReview(new Set());
                    setVisited(new Set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
                    setCurrentPage(1);
                    setTimeLeft((testMeta?.durationMinutes || 180) * 60);
                    startTimeRef.current = Date.now();
                    setShowResultModal(false);
                    setReviewMode(false);
                  }}
                  className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 font-bold py-2.5 rounded-xl text-xs transition-colors flex items-center justify-center gap-1.5 cursor-pointer border border-slate-200 dark:border-slate-700"
                >
                  <RotateCcw className="w-3.5 h-3.5 text-blue-600 dark:text-amber-400" />
                  <span>Retake Test</span>
                </button>

                <Link
                  href="/dashboard"
                  className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 font-bold py-2.5 rounded-xl text-xs transition-colors flex items-center justify-center gap-1.5 border border-slate-200 dark:border-slate-700"
                >
                  <span>My Dashboard</span>
                </Link>
              </div>
            </div>

          </div>
        </div>
      )}

    </div>
  );
}
