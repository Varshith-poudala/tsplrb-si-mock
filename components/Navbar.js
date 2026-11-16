'use client';

import Link from 'next/link';
import { useSession, signOut } from 'next-auth/react';
import { Shield, User, Award, LogOut, Lock, LayoutDashboard, Crown } from 'lucide-react';
import ThemeToggle from '@/components/ThemeToggle';

export default function Navbar() {
  const { data: session } = useSession();
  const isAdmin = session?.user?.role === 'admin';
  const isPaid = session?.user?.isPaid || isAdmin;

  return (
    <header className="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 text-slate-900 dark:text-slate-100 transition-colors">
      <div className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand / Logo */}
        <Link href="/" className="flex items-center gap-2.5 group">
          <div className="w-9 h-9 rounded-lg bg-slate-900 dark:bg-amber-500/10 text-white dark:text-amber-400 flex items-center justify-center font-bold border border-slate-800 dark:border-amber-500/20 shadow-sm transition-transform group-hover:scale-102">
            <Shield className="w-5 h-5 fill-current" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-bold tracking-tight text-base sm:text-lg text-slate-900 dark:text-white">
                TSPLRB SI
              </span>
              <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">
                CBT 2024-25
              </span>
            </div>
            <p className="text-[11px] text-slate-500 dark:text-slate-400 hidden sm:block">
              Sub-Inspector Mock Test Portal
            </p>
          </div>
        </Link>

        {/* Center / Navigation Links */}
        <nav className="hidden md:flex items-center gap-6 text-sm font-medium">
          <Link
            href="/exam/demo-test-50"
            className="text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-amber-400 flex items-center gap-1.5 transition-colors"
          >
            <Award className="w-4 h-4 text-blue-600 dark:text-amber-400" />
            <span>Free Demo Test</span>
          </Link>

          <Link
            href="/dashboard"
            className="text-slate-600 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white flex items-center gap-1.5 transition-colors"
          >
            <LayoutDashboard className="w-4 h-4 text-slate-500 dark:text-slate-400" />
            <span>Dashboard</span>
          </Link>

          {isAdmin && (
            <Link
              href="/admin"
              className="bg-purple-50 dark:bg-purple-950/50 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800 hover:bg-purple-100 dark:hover:bg-purple-900/60 px-2.5 py-1 rounded-md text-xs font-semibold flex items-center gap-1.5 transition-colors"
            >
              <Crown className="w-3.5 h-3.5 text-purple-600 dark:text-amber-400" />
              <span>Admin Panel</span>
            </Link>
          )}
        </nav>

        {/* Right Section: Theme Toggle & User Auth */}
        <div className="flex items-center gap-2.5 sm:gap-3">
          
          {/* Theme Switcher (Light / Dark) */}
          <ThemeToggle />

          {session?.user ? (
            <div className="flex items-center gap-2.5">
              {isPaid ? (
                <span className="hidden sm:inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
                  <Crown className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                  <span>Full Access</span>
                </span>
              ) : (
                <Link
                  href="/#pricing"
                  className="hidden sm:inline-flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-900 dark:bg-amber-500 text-white dark:text-slate-950 hover:bg-slate-800 dark:hover:bg-amber-400 transition-colors shadow-sm"
                >
                  <Lock className="w-3.5 h-3.5" />
                  <span>Unlock ₹99</span>
                </Link>
              )}

              {/* User Avatar & Logout */}
              <div className="flex items-center gap-2 pl-2 border-l border-slate-200 dark:border-slate-800">
                <Link
                  href="/dashboard"
                  className="flex items-center gap-2 text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white"
                  title="Go to Dashboard"
                >
                  <div className="w-8 h-8 rounded-full bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-center text-xs font-bold text-slate-700 dark:text-amber-400">
                    {session.user.name ? session.user.name.charAt(0).toUpperCase() : 'U'}
                  </div>
                  <span className="text-xs font-medium max-w-[100px] truncate hidden lg:inline-block">
                    {session.user.name || session.user.email?.split('@')[0]}
                  </span>
                </Link>

                <button
                  onClick={() => signOut({ callbackUrl: '/' })}
                  className="text-slate-400 hover:text-rose-600 dark:hover:text-rose-400 p-1.5 rounded-md hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
                  title="Sign out"
                >
                  <LogOut className="w-4 h-4" />
                </button>
              </div>
            </div>
          ) : (
            <Link
              href="/login"
              className="bg-slate-900 dark:bg-white text-white dark:text-slate-900 hover:bg-slate-800 dark:hover:bg-slate-100 font-semibold text-xs sm:text-sm px-3.5 py-1.5 sm:py-2 rounded-lg transition-colors shadow-sm flex items-center gap-1.5"
            >
              <User className="w-3.5 h-3.5" />
              <span>Sign In</span>
            </Link>
          )}

        </div>

      </div>
    </header>
  );
}
