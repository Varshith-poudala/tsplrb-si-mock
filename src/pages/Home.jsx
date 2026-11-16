import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Shield, Award, CheckCircle2, Zap, Smartphone, Clock, ArrowRight, Lock, Crown, Check, CreditCard, Loader2, Sparkles, BookOpen, BarChart3, HelpCircle, AlertCircle } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import CheckoutModal from '../components/CheckoutModal';

export default function Home() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [showCheckoutModal, setShowCheckoutModal] = useState(false);

  const isPaid = user?.isPaid || user?.role === 'admin';

  const handleOpenCheckout = () => {
    if (!user) {
      navigate('/login?redirect=checkout');
      return;
    }
    setShowCheckoutModal(true);
  };

  return (
    <div className="flex flex-col min-h-[calc(100vh-4rem)]">
      
      {/* 1. HERO SECTION */}
      <section className="py-12 sm:py-16 md:py-20 px-4 sm:px-6 lg:px-8 max-w-[1440px] mx-auto w-full text-center">
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs font-semibold text-slate-700 dark:text-slate-300 mb-6 shadow-xs">
          <Sparkles className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400" />
          <span>TSPLRB Sub-Inspector Preliminary Written Test (PWT) 2026</span>
        </div>

        <h1 className="text-3xl sm:text-5xl lg:text-6xl font-black text-slate-900 dark:text-white tracking-tight leading-tight max-w-4xl mx-auto">
          Master the TS SI Exam in Official Online CBT Environment
        </h1>

        <p className="mt-4 sm:mt-6 text-sm sm:text-base text-slate-600 dark:text-slate-400 max-w-2xl mx-auto leading-relaxed">
          Full 200-question simulations with official negative marking (-0.20), authentic bilingual questions (English & తెలుగు), 10 questions/page navigation, and instant score analytics.
        </p>

        {/* Hero CTAs */}
        <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
          <Link
            to="/exam/demo-test-50"
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs sm:text-sm px-6 py-3 rounded-xl transition-all shadow-xs flex items-center gap-2"
          >
            <span>Start Free Demo Test (50 Qs)</span>
            <ArrowRight className="w-4 h-4" />
          </Link>

          {isPaid ? (
            <Link
              to="/dashboard"
              className="bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-bold text-xs sm:text-sm px-6 py-3 rounded-xl transition-all shadow-xs flex items-center gap-2"
            >
              <span>Go to Full Dashboard</span>
              <Crown className="w-4 h-4 text-amber-400 dark:text-amber-500" />
            </Link>
          ) : (
            <button
              onClick={handleOpenCheckout}
              className="bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100 font-bold text-xs sm:text-sm px-6 py-3 rounded-xl transition-all shadow-xs flex items-center gap-2 cursor-pointer"
            >
              <Lock className="w-4 h-4 text-slate-400" />
              <span>Unlock All 8 Full Exams (₹99)</span>
            </button>
          )}
        </div>

        {/* Key Features Banner */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mt-12 max-w-4xl mx-auto text-left">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="w-8 h-8 rounded-lg bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400 flex items-center justify-center mb-2">
              <Clock className="w-4 h-4" />
            </div>
            <div className="font-bold text-xs text-slate-900 dark:text-white">3-Hour Timer</div>
            <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Real exam pace countdown with pause & resume</div>
          </div>

          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="w-8 h-8 rounded-lg bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mb-2">
              <CheckCircle2 className="w-4 h-4" />
            </div>
            <div className="font-bold text-xs text-slate-900 dark:text-white">Official Negative Marking</div>
            <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">+1 for correct, -0.20 for wrong response</div>
          </div>

          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="w-8 h-8 rounded-lg bg-purple-50 dark:bg-purple-950/60 text-purple-600 dark:text-purple-400 flex items-center justify-center mb-2">
              <BookOpen className="w-4 h-4" />
            </div>
            <div className="font-bold text-xs text-slate-900 dark:text-white">100% Bilingual</div>
            <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Instant English / తెలుగు language toggle</div>
          </div>

          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="w-8 h-8 rounded-lg bg-amber-50 dark:bg-amber-950/60 text-amber-600 dark:text-amber-400 flex items-center justify-center mb-2">
              <BarChart3 className="w-4 h-4" />
            </div>
            <div className="font-bold text-xs text-slate-900 dark:text-white">Detailed Solutions</div>
            <div className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Section breakdown & step-by-step rationales</div>
          </div>
        </div>
      </section>

      {/* 2. EXAM BLUEPRINT & TEST CATALOG OVERVIEW */}
      <section className="py-12 bg-white dark:bg-slate-900/60 border-y border-slate-200 dark:border-slate-800">
        <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center max-w-2xl mx-auto mb-10">
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">Official TS SI Exam Structure</h2>
            <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">200 Questions divided into three strict syllabus sections</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-6">
              <div className="text-xs font-bold text-blue-600 dark:text-blue-400 uppercase tracking-wider mb-2">Part A • Q1 to Q50</div>
              <h3 className="text-base font-bold text-slate-900 dark:text-white mb-2">Arithmetic & Mensuration</h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mb-4">
                Number systems, LCM/HCF, ratios, profit & loss, simple and compound interest, time & work, pipes & cisterns, speeds, 2D/3D geometry.
              </p>
              <div className="text-xs font-semibold text-slate-500">50 Marks • 50 Questions</div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-6">
              <div className="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider mb-2">Part B • Q51 to Q100</div>
              <h3 className="text-base font-bold text-slate-900 dark:text-white mb-2">Reasoning & Mental Ability</h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mb-4">
                Syllogisms, blood relations, coding-decoding, direction tests, seating arrangements, non-verbal matrices, data sufficiency.
              </p>
              <div className="text-xs font-semibold text-slate-500">50 Marks • 50 Questions</div>
            </div>

            <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-2xl p-6">
              <div className="text-xs font-bold text-purple-600 dark:text-purple-400 uppercase tracking-wider mb-2">Part C • Q101 to Q200</div>
              <h3 className="text-base font-bold text-slate-900 dark:text-white mb-2">General Studies & Telangana Movement</h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed mb-4">
                Indian Constitution, Telangana Movement (1948–2014), Mulki rules, Gentlemen's Agreement, State policy schemes, Geography, and Current Affairs.
              </p>
              <div className="text-xs font-semibold text-slate-500">100 Marks • 100 Questions</div>
            </div>
          </div>
        </div>
      </section>

      {/* 3. PRICING SECTION */}
      <section id="pricing" className="py-16 px-4 sm:px-6 lg:px-8 max-w-4xl mx-auto w-full text-center">
        <h2 className="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white">Affordable, Candidate-First Pricing</h2>
        <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1 mb-8">One-time payment for lifetime access to all 8 full exam papers (1 Demo + 7 Full 200-Q Papers)</p>

        <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-8 max-w-md mx-auto shadow-sm text-left">
          <div className="flex items-center justify-between mb-4">
            <span className="text-xs font-bold px-3 py-1 rounded-full bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800">
              COMPLETE TEST SERIES
            </span>
            <div className="text-right">
              <span className="text-xs text-slate-400 line-through mr-2">₹499</span>
              <span className="text-3xl font-black text-slate-900 dark:text-white">₹99</span>
            </div>
          </div>

          <div className="space-y-3 mb-6 text-xs text-slate-600 dark:text-slate-300">
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Free 50-Question Diagnostic Demo Mock</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Mock Test 3 (Easy • Foundational 200 Qs)</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Mock Test 1 (Official 200-Question Blueprint)</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Mock Test 2 (High-Yield Practice 200 Qs)</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Mock Test 4 (Medium • 2022 Official PYQ Calibration)</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Mock Test 5 (Hard • Advanced High-Yield Simulation)</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Mock Test 6 (Medium • Speed & Accuracy Focus 200 Qs)</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Mock Test 7 (Hard • Grand Master Championship 200 Qs)</span>
            </div>
            <div className="flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-500 flex-shrink-0" />
              <span>Unlimited retakes, attempts history & bilingual solutions</span>
            </div>
          </div>

          {isPaid ? (
            <Link
              to="/dashboard"
              className="block w-full text-center bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs py-3 rounded-xl transition-colors shadow-xs"
            >
              Full Access Active • Open Dashboard
            </Link>
          ) : (
            <button
              onClick={handleOpenCheckout}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-3 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-2 cursor-pointer"
            >
              <CreditCard className="w-4 h-4" />
              <span>Pay ₹99 via UPI / Card / NetBanking</span>
            </button>
          )}

          <div className="mt-4 text-center text-[11px] text-slate-400">
            Secure 256-bit encrypted checkout powered by Razorpay
          </div>
        </div>
      </section>

      {/* Checkout Modal */}
      <CheckoutModal
        isOpen={showCheckoutModal}
        onClose={() => setShowCheckoutModal(false)}
      />

    </div>
  );
}
