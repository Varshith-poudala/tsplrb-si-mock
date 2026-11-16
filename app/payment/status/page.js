'use client';

import { Suspense, useEffect } from 'react';
import { useSearchParams } from 'next/navigation';
import Navbar from '@/components/Navbar';
import Link from 'next/link';
import { CheckCircle2, ArrowRight, Crown } from 'lucide-react';
import confetti from 'canvas-confetti';

function PaymentStatusContent() {
  const searchParams = useSearchParams();
  const txnId = searchParams.get('id');

  useEffect(() => {
    try {
      confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
    } catch (e) {}
  }, [txnId]);

  return (
    <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-8 text-center shadow-lg relative">
      <div className="w-12 h-12 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-600 dark:text-emerald-400 rounded-xl flex items-center justify-center mx-auto mb-4 border border-emerald-200 dark:border-emerald-800 shadow-xs">
        <CheckCircle2 className="w-6 h-6" />
      </div>

      <h1 className="text-xl font-bold text-slate-900 dark:text-white">Payment Successful</h1>
      <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 mb-6">
        Transaction ID: <span className="font-mono text-slate-700 dark:text-slate-300 font-semibold">{txnId || 'TXN_SUCCESS'}</span>
      </p>

      <div className="bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800 rounded-xl p-4 text-xs text-emerald-900 dark:text-emerald-200 mb-6 flex items-center gap-3 text-left">
        <Crown className="w-5 h-5 text-emerald-600 dark:text-amber-400 flex-shrink-0" />
        <div>
          <div className="font-bold text-emerald-900 dark:text-emerald-300">All Full-Length Exams Unlocked</div>
          <div className="text-[11px] text-emerald-700 dark:text-emerald-400/90 mt-0.5">
            You now have unlimited attempts on all 200-question mock exams and in-depth solutions!
          </div>
        </div>
      </div>

      <div className="space-y-2.5">
        <Link
          href="/dashboard"
          className="w-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100 font-bold py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-2 text-xs"
        >
          <span>Go to Candidate Dashboard</span>
          <ArrowRight className="w-3.5 h-3.5" />
        </Link>

        <Link
          href="/exam/tsplrb-si-mock-full-200"
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-2 text-xs"
        >
          <span>Start Full 200-Question Exam 1</span>
        </Link>
      </div>
    </div>
  );
}

export default function PaymentStatusPage() {
  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col transition-colors">
      <Navbar />
      <main className="flex-1 flex items-center justify-center p-4 py-12">
        <Suspense fallback={<div className="text-slate-500 text-xs">Loading payment status...</div>}>
          <PaymentStatusContent />
        </Suspense>
      </main>
    </div>
  );
}
