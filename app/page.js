'use client';

import { useState } from 'react';
import Link from 'next/link';
import Navbar from '@/components/Navbar';
import { Shield, Award, CheckCircle2, Zap, Smartphone, Clock, ArrowRight, Lock, Crown, Check, CreditCard, Loader2, Sparkles, BookOpen, BarChart3, HelpCircle } from 'lucide-react';
import { useSession } from 'next-auth/react';

export default function HomePage() {
  const { data: session } = useSession();
  const [showPayModal, setShowPayModal] = useState(false);
  const [payingRazorpay, setPayingRazorpay] = useState(false);
  const [utrInput, setUtrInput] = useState('');
  const [verifyingUtr, setVerifyingUtr] = useState(false);
  const [utrStatus, setUtrStatus] = useState(null);

  const isPaid = session?.user?.isPaid || session?.user?.role === 'admin';

  // Load Razorpay Checkout Script
  const loadRazorpayScript = () => {
    return new Promise((resolve) => {
      if (typeof window !== 'undefined' && window.Razorpay) {
        return resolve(true);
      }
      const script = document.createElement('script');
      script.src = 'https://checkout.razorpay.com/v1/checkout.js';
      script.onload = () => resolve(true);
      script.onerror = () => resolve(false);
      document.body.appendChild(script);
    });
  };

  // Razorpay 1-Click Checkout with Auto-Redirect
  const handleRazorpayPayment = async () => {
    if (!session?.user) {
      window.location.href = '/login?callbackUrl=' + encodeURIComponent(window.location.pathname);
      return;
    }

    setPayingRazorpay(true);
    try {
      const isLoaded = await loadRazorpayScript();
      if (!isLoaded) {
        throw new Error('Failed to load Razorpay payment gateway SDK.');
      }

      // 1. Create Order on Backend
      const orderRes = await fetch('/api/payment/razorpay/create-order', {
        method: 'POST',
      });
      const orderData = await orderRes.json();
      if (!orderRes.ok) {
        throw new Error(orderData.error || 'Failed to create order');
      }

      // 2. Open Razorpay Checkout Modal
      const options = {
        key: orderData.keyId,
        amount: orderData.amount,
        currency: orderData.currency,
        name: 'TSPLRB SI Mock Test Series',
        description: 'Full Lifetime Access to All 200-Question Exams',
        order_id: orderData.orderId,
        prefill: {
          name: session?.user?.name || '',
          email: session?.user?.email || '',
        },
        theme: {
          color: '#0f172a', // Clean Professional Navy
        },
        handler: async function (response) {
          try {
            // 3. Cryptographically verify payment on server
            const verifyRes = await fetch('/api/payment/razorpay/verify', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                razorpay_order_id: response.razorpay_order_id,
                razorpay_payment_id: response.razorpay_payment_id,
                razorpay_signature: response.razorpay_signature,
              }),
            });

            const verifyData = await verifyRes.json();

            if (verifyData.success) {
              window.location.href = `/payment/status?id=${response.razorpay_payment_id}`;
            } else {
              alert('Payment verification failed: ' + verifyData.error);
            }
          } catch (verErr) {
            alert('Verification network error: ' + verErr.message);
          }
        },
        modal: {
          ondismiss: function () {
            setPayingRazorpay(false);
          },
        },
      };

      const razorpayInstance = new window.Razorpay(options);
      razorpayInstance.open();
    } catch (err) {
      alert(err.message);
    } finally {
      setPayingRazorpay(false);
    }
  };

  // Manual UTR Verification handler
  const handleVerifyUtr = async (e) => {
    e.preventDefault();
    if (!utrInput || utrInput.length < 8) return;
    setVerifyingUtr(true);
    setUtrStatus(null);
    try {
      const res = await fetch('/api/payment/verify-utr', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ utrNumber: utrInput }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Verification failed');
      setUtrStatus({ success: true, message: data.message });
    } catch (err) {
      setUtrStatus({ success: false, message: err.message });
    } finally {
      setVerifyingUtr(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col transition-colors">
      <Navbar />

      {/* 1. HERO SECTION (Clean, Minimalist, High Contrast) */}
      <section className="pt-12 pb-16 sm:pt-20 sm:pb-24 border-b border-slate-200 dark:border-slate-850">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 text-center">
          
          {/* Subtle Badge */}
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 text-xs font-semibold mb-6 shadow-xs">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>2024-25 Telangana Police Recruitment Pattern</span>
          </div>

          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-black text-slate-900 dark:text-white tracking-tight leading-tight">
            Telangana Police Sub-Inspector <br className="hidden sm:inline" />
            <span className="text-blue-600 dark:text-amber-400">
              Preliminary Mock Test Series
            </span>
          </h1>

          <p className="mt-5 text-sm sm:text-base lg:text-lg text-slate-600 dark:text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Practice with official TCS-iON pattern CBT exams. 200 questions, bilingual (English & Telugu), -0.20 negative marking, live 3-hour timer, and diagnostic analytics.
          </p>

          {/* Action CTAs */}
          <div className="mt-8 flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-4 max-w-md mx-auto sm:max-w-none">
            
            {/* Free Demo CTA */}
            <Link
              href="/exam/demo-test-50"
              className="w-full sm:w-auto bg-blue-600 hover:bg-blue-700 text-white font-bold px-7 py-3.5 rounded-xl transition-all shadow-sm hover:shadow flex items-center justify-center gap-2 text-sm"
            >
              <Award className="w-4 h-4 text-blue-200" />
              <span>Take Free Demo Test (50 Qs)</span>
              <ArrowRight className="w-4 h-4" />
            </Link>

            {/* Unlock Full Series CTA */}
            {isPaid ? (
              <Link
                href="/dashboard"
                className="w-full sm:w-auto bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-7 py-3.5 rounded-xl transition-all shadow-sm flex items-center justify-center gap-2 text-sm"
              >
                <Crown className="w-4 h-4 text-emerald-200" />
                <span>Go to My Dashboard</span>
              </Link>
            ) : (
              <button
                onClick={handleRazorpayPayment}
                disabled={payingRazorpay}
                className="w-full sm:w-auto bg-slate-900 dark:bg-white text-white dark:text-slate-950 hover:bg-slate-800 dark:hover:bg-slate-100 font-bold px-7 py-3.5 rounded-xl transition-all shadow-sm flex items-center justify-center gap-2 text-sm disabled:opacity-50 cursor-pointer"
              >
                {payingRazorpay ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Connecting to Gateway...</span>
                  </>
                ) : (
                  <>
                    <Lock className="w-4 h-4" />
                    <span>Unlock Full Series (₹99)</span>
                  </>
                )}
              </button>
            )}

          </div>

          {/* Highlights strip */}
          <div className="mt-10 pt-8 border-t border-slate-200 dark:border-slate-850 grid grid-cols-2 sm:grid-cols-4 gap-4 text-left">
            <div className="p-3 rounded-lg bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
              <div className="text-xs text-slate-500 dark:text-slate-400">Exam Format</div>
              <div className="text-sm font-bold text-slate-900 dark:text-white mt-0.5">200 Questions / 3 Hrs</div>
            </div>
            <div className="p-3 rounded-lg bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
              <div className="text-xs text-slate-500 dark:text-slate-400">Language</div>
              <div className="text-sm font-bold text-slate-900 dark:text-white mt-0.5">English & Telugu</div>
            </div>
            <div className="p-3 rounded-lg bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
              <div className="text-xs text-slate-500 dark:text-slate-400">Marking Scheme</div>
              <div className="text-sm font-bold text-slate-900 dark:text-white mt-0.5">+1 Mark / -0.20 Negative</div>
            </div>
            <div className="p-3 rounded-lg bg-white dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
              <div className="text-xs text-slate-500 dark:text-slate-400">Attempts</div>
              <div className="text-sm font-bold text-slate-900 dark:text-white mt-0.5">Unlimited Re-takes</div>
            </div>
          </div>

        </div>
      </section>

      {/* 2. SYLLABUS BREAKDOWN (Clean Grid) */}
      <section className="py-14 bg-white dark:bg-slate-900/40 border-b border-slate-200 dark:border-slate-850">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          
          <div className="text-center max-w-xl mx-auto mb-10">
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
              Official TSPLRB SI Exam Syllabus (200 Marks)
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
              Strictly aligned with the Telangana State Level Police Recruitment Board guidelines
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            
            <div className="bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-xs">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-bold text-blue-600 dark:text-blue-400 uppercase tracking-wider">Part A</span>
                <span className="bg-blue-100 dark:bg-blue-950/60 text-blue-800 dark:text-blue-300 text-xs font-semibold px-2 py-0.5 rounded border border-blue-200 dark:border-blue-900">
                  50 Questions
                </span>
              </div>
              <h3 className="font-bold text-slate-900 dark:text-white text-base">Arithmetic</h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
                Number Systems, LCM/HCF, Percentages, Profit & Loss, Simple & Compound Interest, Time & Work, Time & Distance, Ratios, 2D/3D Mensuration.
              </p>
            </div>

            <div className="bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-xs">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-bold text-purple-600 dark:text-purple-400 uppercase tracking-wider">Part B</span>
                <span className="bg-purple-100 dark:bg-purple-950/60 text-purple-800 dark:text-purple-300 text-xs font-semibold px-2 py-0.5 rounded border border-purple-200 dark:border-purple-900">
                  50 Questions
                </span>
              </div>
              <h3 className="font-bold text-slate-900 dark:text-white text-base">Reasoning & Mental Ability</h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
                Coding-Decoding, Blood Relations, Syllogisms, Direction Sense, Numerical Series, Analogy, Puzzles, Seating Arrangements, Non-verbal figures.
              </p>
            </div>

            <div className="bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-xs">
              <div className="flex items-center justify-between mb-3">
                <span className="text-xs font-bold text-amber-600 dark:text-amber-400 uppercase tracking-wider">Part C</span>
                <span className="bg-amber-100 dark:bg-amber-950/60 text-amber-800 dark:text-amber-300 text-xs font-semibold px-2 py-0.5 rounded border border-amber-200 dark:border-amber-900">
                  100 Questions
                </span>
              </div>
              <h3 className="font-bold text-slate-900 dark:text-white text-base">General Studies & Telangana Movement</h3>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
                2024 Current Affairs (HYDRAA, Skills Univ, G20), Everyday Science, Indian History & Polity, Geography, Telangana History & Formation Movement.
              </p>
            </div>

          </div>

        </div>
      </section>

      {/* 3. PLATFORM FEATURES (Minimalist Cards) */}
      <section className="py-16">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          
          <div className="text-center max-w-xl mx-auto mb-12">
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
              Built for Real Exam Performance
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
              Engineered with the exact look and feel of the official TCS-iON computer-based test
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
            
            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-xs">
              <div className="w-9 h-9 rounded-lg bg-blue-50 dark:bg-blue-950/50 text-blue-600 dark:text-blue-400 flex items-center justify-center mb-3">
                <Smartphone className="w-5 h-5" />
              </div>
              <h4 className="font-bold text-slate-900 dark:text-white text-sm">Mobile Optimized</h4>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-1.5 leading-relaxed">
                Engineered for smartphones. Bottom thumb navigation, high-contrast Telugu fonts, zero lag.
              </p>
            </div>

            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-xs">
              <div className="w-9 h-9 rounded-lg bg-amber-50 dark:bg-amber-950/50 text-amber-600 dark:text-amber-400 flex items-center justify-center mb-3">
                <Clock className="w-5 h-5" />
              </div>
              <h4 className="font-bold text-slate-900 dark:text-white text-sm">Real 3-Hour Simulation</h4>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-1.5 leading-relaxed">
                Live countdown timer with -0.20 negative marking calculation to hone time management under pressure.
              </p>
            </div>

            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-xs">
              <div className="w-9 h-9 rounded-lg bg-emerald-50 dark:bg-emerald-950/50 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mb-3">
                <Shield className="w-5 h-5" />
              </div>
              <h4 className="font-bold text-slate-900 dark:text-white text-sm">Anti-Cheat Architecture</h4>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-1.5 leading-relaxed">
                Correct answers are stored server-side until completion. Inspect element reveals zero answers.
              </p>
            </div>

            <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 shadow-xs">
              <div className="w-9 h-9 rounded-lg bg-purple-50 dark:bg-purple-950/50 text-purple-600 dark:text-purple-400 flex items-center justify-center mb-3">
                <BarChart3 className="w-5 h-5" />
              </div>
              <h4 className="font-bold text-slate-900 dark:text-white text-sm">Analytics & Retakes</h4>
              <p className="text-xs text-slate-600 dark:text-slate-400 mt-1.5 leading-relaxed">
                Re-take exams infinitely. Review detailed solutions and Telugu explanations for every question.
              </p>
            </div>

          </div>

        </div>
      </section>

      {/* 4. PRICING SECTION (Clean, Minimalist, High Trust) */}
      <section id="pricing" className="py-16 bg-white dark:bg-slate-900/40 border-y border-slate-200 dark:border-slate-850">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 text-center">
          
          <h2 className="text-2xl sm:text-3xl font-bold text-slate-900 dark:text-white">
            Simple, Transparent Pricing
          </h2>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
            One-time payment. Lifetime access. No recurring subscriptions.
          </p>

          <div className="mt-10 grid grid-cols-1 md:grid-cols-2 gap-6 max-w-2xl mx-auto text-left">
            
            {/* Free Tier Card */}
            <div className="bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-7 flex flex-col justify-between shadow-xs">
              <div>
                <div className="text-xs font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">
                  Starter Pack
                </div>
                <h3 className="text-xl font-bold text-slate-900 dark:text-white">Free Demo Mock</h3>
                
                <div className="text-3xl font-black text-slate-900 dark:text-white mt-4">₹0</div>
                <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">No payment or card required</div>

                <ul className="mt-6 space-y-3 text-xs text-slate-600 dark:text-slate-300">
                  <li className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                    <span>50-Question Free Demo Paper</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                    <span>Bilingual (English & Telugu)</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                    <span>Instant Score & In-depth Solutions</span>
                  </li>
                </ul>
              </div>

              <Link
                href="/exam/demo-test-50"
                className="mt-8 block w-full bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 text-slate-900 dark:text-white font-bold py-2.5 rounded-xl text-center text-xs transition-colors"
              >
                Start Free Demo Test
              </Link>
            </div>

            {/* Paid Full Pass Card (₹99) */}
            <div className="bg-white dark:bg-slate-900 border-2 border-slate-900 dark:border-amber-400/80 rounded-2xl p-6 sm:p-7 flex flex-col justify-between relative shadow-md">
              <div className="absolute -top-3 right-6 bg-slate-900 dark:bg-amber-400 text-white dark:text-slate-950 text-[10px] font-bold uppercase px-2.5 py-0.5 rounded-full shadow-xs">
                Complete Pass
              </div>

              <div>
                <div className="text-xs font-bold text-blue-600 dark:text-amber-400 uppercase tracking-wider mb-1">
                  Full Access
                </div>
                <h3 className="text-xl font-bold text-slate-900 dark:text-white">TSPLRB SI Complete Series</h3>
                
                <div className="flex items-baseline gap-2 mt-4">
                  <span className="text-3xl font-black text-slate-900 dark:text-white">₹99</span>
                  <span className="text-sm text-slate-400 line-through">₹499</span>
                  <span className="text-[11px] font-semibold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/50 px-2 py-0.5 rounded border border-emerald-200 dark:border-emerald-800">
                    80% OFF
                  </span>
                </div>
                <div className="text-xs text-slate-500 dark:text-slate-400 mt-1">One-time payment • Lifetime access</div>

                <ul className="mt-6 space-y-3 text-xs text-slate-700 dark:text-slate-300">
                  <li className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                    <span className="font-semibold text-slate-900 dark:text-white">All Full-Length 200-Question Exams</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                    <span>Unlimited Exam Re-takes</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                    <span>Personal Candidate Performance Dashboard</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <Check className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
                    <span>In-depth Solutions & Telugu Explanations</span>
                  </li>
                </ul>
              </div>

              {isPaid ? (
                <Link
                  href="/dashboard"
                  className="mt-8 block w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3 rounded-xl text-center text-xs transition-colors shadow-sm"
                >
                  Access Unlocked • View Dashboard
                </Link>
              ) : (
                <div className="mt-8 space-y-2">
                  <button
                    onClick={handleRazorpayPayment}
                    disabled={payingRazorpay}
                    className="w-full bg-slate-900 dark:bg-amber-400 text-white dark:text-slate-950 hover:bg-slate-800 dark:hover:bg-amber-300 font-bold py-3 rounded-xl text-center text-xs transition-all shadow-sm flex items-center justify-center gap-2 disabled:opacity-50 cursor-pointer"
                  >
                    {payingRazorpay ? (
                      <>
                        <Loader2 className="w-4 h-4 animate-spin" />
                        <span>Connecting to Gateway...</span>
                      </>
                    ) : (
                      <>
                        <CreditCard className="w-4 h-4" />
                        <span>Pay ₹99 Online (UPI / Cards / NetBanking)</span>
                      </>
                    )}
                  </button>

                  <button
                    onClick={() => setShowPayModal(true)}
                    className="w-full text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 text-[11px] font-medium py-1 text-center transition-colors underline cursor-pointer"
                  >
                    Or Pay via Direct PhonePe QR Code
                  </button>
                </div>
              )}
            </div>

          </div>

        </div>
      </section>

      {/* 5. DIRECT PHONEPE QR MODAL (Clean Fallback) */}
      {showPayModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-xs">
          <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-7 shadow-2xl relative">
            
            <button
              onClick={() => setShowPayModal(false)}
              className="absolute top-4 right-4 text-slate-400 hover:text-slate-700 dark:hover:text-white p-1 text-sm font-bold cursor-pointer"
            >
              ✕
            </button>

            <div className="text-center mb-5">
              <div className="w-10 h-10 bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-amber-400 rounded-xl flex items-center justify-center mx-auto mb-2 border border-slate-200 dark:border-slate-700">
                <Crown className="w-5 h-5" />
              </div>
              <h3 className="text-base font-bold text-slate-900 dark:text-white">Direct PhonePe QR Code</h3>
              <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Scan with PhonePe, GPay, or Paytm to pay ₹99</p>
            </div>

            {/* UPI QR Code */}
            <div className="bg-white p-3 rounded-xl mx-auto w-44 h-44 flex items-center justify-center border border-slate-200 dark:border-slate-700 mb-3">
              <img
                src={`https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=${encodeURIComponent('upi://pay?pa=varshithpoudala@ybl&pn=TSPLRB_SI_Mock&am=99&cu=INR&tn=TSPLRB_SI_Full_Access')}`}
                alt="PhonePe UPI QR Code"
                className="w-full h-full object-contain"
              />
            </div>

            <div className="text-center text-xs text-slate-600 dark:text-slate-400 mb-4">
              UPI ID: <span className="font-mono font-bold text-slate-900 dark:text-amber-400">varshithpoudala@ybl</span>
            </div>

            {/* Submit UTR verification form */}
            <form onSubmit={handleVerifyUtr} className="pt-4 border-t border-slate-200 dark:border-slate-800">
              <div className="text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1.5">
                Enter 12-Digit UPI Reference (UTR) Number:
              </div>
              <div className="flex gap-2">
                <input
                  type="text"
                  placeholder="e.g. 431289104812"
                  value={utrInput}
                  onChange={(e) => setUtrInput(e.target.value)}
                  className="flex-1 bg-slate-50 dark:bg-slate-950 border border-slate-300 dark:border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-blue-600"
                />
                <button
                  type="submit"
                  disabled={verifyingUtr || !utrInput}
                  className="bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-bold px-3 py-2 rounded-lg text-xs disabled:opacity-50 transition-colors cursor-pointer"
                >
                  {verifyingUtr ? 'Submitting...' : 'Submit'}
                </button>
              </div>

              {utrStatus && (
                <div className={`mt-2 text-xs font-medium ${utrStatus.success ? 'text-emerald-600 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'}`}>
                  {utrStatus.message}
                </div>
              )}
            </form>

          </div>
        </div>
      )}

      {/* 6. FOOTER */}
      <footer className="mt-auto py-8 bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 text-center text-xs text-slate-500 dark:text-slate-400 transition-colors">
        <div className="max-w-6xl mx-auto px-4">
          <p>© 2024-2026 TSPLRB SI Exam Preparation Portal. Built for Telangana Police Aspirants.</p>
          <p className="mt-1 text-[11px] text-slate-400 dark:text-slate-500">
            Official syllabus: Arithmetic (50 Qs) • Reasoning & Mental Ability (50 Qs) • General Studies & Telangana Movement (100 Qs).
          </p>
        </div>
      </footer>

    </div>
  );
}
