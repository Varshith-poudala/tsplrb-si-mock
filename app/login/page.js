'use client';

import { useState } from 'react';
import { signIn } from 'next-auth/react';
import Navbar from '@/components/Navbar';
import { Shield, Lock, ArrowRight, Mail, User } from 'lucide-react';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [loading, setLoading] = useState(false);

  const handleDevLogin = async (e) => {
    e.preventDefault();
    if (!email) return;
    setLoading(true);
    await signIn('dev-login', {
      email,
      name,
      callbackUrl: email.toLowerCase() === 'varshithpoudala@gmail.com' ? '/admin' : '/dashboard',
    });
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col transition-colors">
      <Navbar />

      <main className="flex-1 flex items-center justify-center p-4 py-12">
        <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-6 sm:p-8 shadow-sm">
          
          {/* Emblem */}
          <div className="w-12 h-12 bg-slate-900 dark:bg-amber-400/10 text-white dark:text-amber-400 rounded-xl flex items-center justify-center font-bold border border-slate-800 dark:border-amber-400/20 shadow-xs mx-auto mb-4">
            <Shield className="w-6 h-6 fill-current" />
          </div>

          <div className="text-center mb-6">
            <h1 className="text-xl font-bold text-slate-900 dark:text-white">Sign In to TSPLRB SI Portal</h1>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">Access your mock tests, attempt history, and analytics</p>
          </div>

          {/* 1. Google Login */}
          <button
            onClick={() => signIn('google', { callbackUrl: '/dashboard' })}
            className="w-full bg-white hover:bg-slate-50 border border-slate-200 text-slate-800 font-semibold py-2.5 px-4 rounded-xl flex items-center justify-center gap-2.5 transition-colors shadow-xs text-xs sm:text-sm mb-4 cursor-pointer"
          >
            <svg className="w-4 h-4" viewBox="0 0 24 24">
              <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
              <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
              <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z" />
              <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z" />
            </svg>
            Continue with Google
          </button>

          <div className="relative flex py-2 items-center mb-4">
            <div className="flex-grow border-t border-slate-200 dark:border-slate-800"></div>
            <span className="flex-shrink mx-3 text-slate-400 dark:text-slate-500 text-[11px] uppercase font-semibold">Or Direct Sign In</span>
            <div className="flex-grow border-t border-slate-200 dark:border-slate-800"></div>
          </div>

          {/* 2. Direct Sign In */}
          <form onSubmit={handleDevLogin} className="space-y-3">
            <div>
              <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">Email Address</label>
              <div className="relative">
                <Mail className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="e.g. candidate@gmail.com"
                  required
                  className="w-full bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-750 rounded-lg pl-9 pr-3 py-2 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-blue-600"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">Your Name (Optional)</label>
              <div className="relative">
                <User className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="e.g. Varshith"
                  className="w-full bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-750 rounded-lg pl-9 pr-3 py-2 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-blue-600"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading || !email}
              className="w-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100 font-bold py-2.5 rounded-lg transition-colors shadow-xs flex items-center justify-center gap-2 text-xs disabled:opacity-50 cursor-pointer"
            >
              <span>{loading ? 'Signing in...' : 'Sign In with Email'}</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </form>

          {/* Quick preset accounts */}
          <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800">
            <div className="text-[11px] text-slate-500 dark:text-slate-400 mb-2 font-medium">Quick 1-Click Accounts:</div>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => {
                  setEmail('varshithpoudala@gmail.com');
                  setName('Varshith (Admin)');
                }}
                className="bg-purple-50 dark:bg-purple-950/40 hover:bg-purple-100 dark:hover:bg-purple-900/60 border border-purple-200 dark:border-purple-800 text-purple-900 dark:text-purple-200 text-xs p-2.5 rounded-lg text-left cursor-pointer"
              >
                <div className="font-bold text-[11px]">👑 Super Admin</div>
                <div className="text-[10px] text-purple-600 dark:text-purple-400 truncate">varshithpoudala@gmail.com</div>
              </button>

              <button
                type="button"
                onClick={() => {
                  setEmail('student_demo@gmail.com');
                  setName('Student Candidate');
                }}
                className="bg-slate-50 dark:bg-slate-800 hover:bg-slate-100 dark:hover:bg-slate-700 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 text-xs p-2.5 rounded-lg text-left cursor-pointer"
              >
                <div className="font-bold text-[11px]">🎓 Free Student</div>
                <div className="text-[10px] text-slate-500 dark:text-slate-400 truncate">student_demo@gmail.com</div>
              </button>
            </div>
          </div>

          <div className="mt-5 flex items-center justify-center gap-1 text-[11px] text-slate-400">
            <Lock className="w-3 h-3" />
            <span>Secure session authentication.</span>
          </div>

        </div>
      </main>
    </div>
  );
}
