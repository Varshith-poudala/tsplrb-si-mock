import React from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { CheckCircle2, XCircle, ArrowRight, ShieldCheck, Crown } from 'lucide-react';

export default function PaymentStatus() {
  const [searchParams] = useSearchParams();
  const status = searchParams.get('status');
  const paymentId = searchParams.get('payment_id');

  const isSuccess = status === 'success';

  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-8 text-center shadow-sm">
        
        {isSuccess ? (
          <>
            <div className="w-14 h-14 bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-emerald-200 dark:border-emerald-800">
              <CheckCircle2 className="w-8 h-8" />
            </div>

            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 text-xs font-bold mb-3 border border-emerald-200">
              <Crown className="w-3.5 h-3.5" />
              <span>Full Access Activated</span>
            </div>

            <h1 className="text-xl font-bold text-slate-900 dark:text-white mb-2">Payment Successful!</h1>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
              Your transaction has been verified. All 5 full 200-question mock tests are unlocked permanently on your account.
            </p>

            {paymentId && (
              <div className="bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 p-3 rounded-xl mb-6 text-xs text-slate-500">
                <span className="font-semibold text-slate-700 dark:text-slate-300">Payment Reference: </span>
                <span className="font-mono text-blue-600">{paymentId}</span>
              </div>
            )}

            <Link
              to="/dashboard"
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-3 rounded-xl transition-colors shadow-xs flex items-center justify-center gap-1.5"
            >
              <span>Go to Candidate Dashboard</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
          </>
        ) : (
          <>
            <div className="w-14 h-14 bg-rose-50 text-rose-600 rounded-2xl flex items-center justify-center mx-auto mb-4 border border-rose-200">
              <XCircle className="w-8 h-8" />
            </div>

            <h1 className="text-xl font-bold text-slate-900 dark:text-white mb-2">Payment Incomplete</h1>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
              We couldn't verify your payment transaction. If your money was deducted, it will automatically refund or be activated shortly.
            </p>

            <div className="space-y-3">
              <Link
                to="/#pricing"
                className="block w-full bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-3 rounded-xl transition-colors"
              >
                Try Payment Again
              </Link>
              <Link
                to="/dashboard"
                className="block w-full bg-slate-100 text-slate-700 font-semibold text-xs py-2.5 rounded-xl hover:bg-slate-200 transition-colors"
              >
                Back to Dashboard
              </Link>
            </div>
          </>
        )}

      </div>
    </div>
  );
}
