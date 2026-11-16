import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { Shield, Sun, Moon, LogIn, LogOut, Crown, LayoutDashboard, BookOpen, KeyRound, ChevronDown } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import ChangePasswordModal from './ChangePasswordModal';

export default function Navbar() {
  const { user, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const [showChangePwModal, setShowChangePwModal] = useState(false);
  const [showSignOutConfirm, setShowSignOutConfirm] = useState(false);
  const [showAccountMenu, setShowAccountMenu] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  const isExamPage = location.pathname.startsWith('/exam');
  if (isExamPage) return null; // Exam interface renders its own focused, distraction-free header

  const isAdmin = user?.role === 'admin' && user?.email?.toLowerCase().trim() === 'varshithpoudala@gmail.com';
  const isPaid = user?.isPaid || isAdmin;

  const searchParams = new URLSearchParams(location.search);
  const isTestsTab = location.pathname === '/dashboard' && searchParams.get('tab') === 'tests';
  const isDashboardTab = location.pathname === '/dashboard' && !isTestsTab;

  return (
    <>
      <header className="bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 sticky top-0 z-40 transition-colors">
        <div className="max-w-[1440px] mx-auto px-3 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-1 sm:gap-4">
          
          {/* Brand / Logo */}
          <Link to="/" className="flex items-center gap-2 sm:gap-3 group flex-shrink-0">
            <div className="w-8 h-8 sm:w-10 sm:h-10 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 flex items-center justify-center shadow-xs transition-transform group-hover:scale-105">
              <Shield className="w-4 h-4 sm:w-5 sm:h-5 fill-current" />
            </div>
            <div>
              <div className="flex items-center gap-1.5 sm:gap-2">
                <span className="font-extrabold text-slate-900 dark:text-white text-sm sm:base tracking-tight">
                  TSPLRB SI
                </span>
                <span className="text-[10px] font-bold px-1.5 sm:px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hidden sm:inline-flex">
                  CBT 2026
                </span>
              </div>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block">Sub-Inspector Mock Test Portal</p>
            </div>
          </Link>

          {/* Center Navigation Tabs: Dashboard vs Tests */}
          <nav className="flex items-center gap-0.5 sm:gap-1 p-0.5 sm:p-1 bg-slate-100 dark:bg-slate-800/80 rounded-xl border border-slate-200/80 dark:border-slate-700/80 text-xs font-bold flex-shrink-0">
            <Link
              to="/dashboard"
              className={`flex items-center gap-1 sm:gap-1.5 px-2.5 sm:px-3.5 py-1 sm:py-1.5 rounded-lg transition-all ${
                isDashboardTab
                  ? 'bg-white dark:bg-slate-900 text-blue-600 dark:text-blue-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <LayoutDashboard className="w-3.5 h-3.5" />
              <span>Dashboard</span>
            </Link>
            <Link
              to="/dashboard?tab=tests"
              className={`flex items-center gap-1 sm:gap-1.5 px-2.5 sm:px-3.5 py-1 sm:py-1.5 rounded-lg transition-all ${
                isTestsTab
                  ? 'bg-white dark:bg-slate-900 text-blue-600 dark:text-blue-400 shadow-xs'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Tests</span>
            </Link>
            {isAdmin && (
              <Link
                to="/admin"
                className={`flex items-center gap-1 sm:gap-1.5 px-2.5 sm:px-3 py-1 sm:py-1.5 rounded-lg text-xs font-bold transition-all ${
                  location.pathname === '/admin'
                    ? 'bg-purple-600 text-white shadow-xs'
                    : 'text-purple-600 dark:text-purple-400 hover:bg-purple-50 dark:hover:bg-purple-950/60'
                }`}
              >
                <Shield className="w-3.5 h-3.5" />
                <span>Admin</span>
              </Link>
            )}
          </nav>

          {/* Right Section: Theme Toggle + User Avatar with Crown & Options */}
          <div className="flex items-center gap-1 sm:gap-3 flex-shrink-0">
            
            {/* Light / Dark Mode Toggle */}
            <button
              onClick={toggleTheme}
              aria-label="Toggle Theme"
              className="w-8 h-8 sm:w-9 sm:h-9 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 flex items-center justify-center hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
            >
              {theme === 'dark' ? <Sun className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-amber-400" /> : <Moon className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-slate-700" />}
            </button>

            {/* User Profile / Auth Action */}
            {user ? (
              <div className="relative flex items-center gap-1 sm:gap-2">
                
                {/* Avatar decorated with Crown on hover */}
                <div 
                  className="relative group cursor-pointer"
                  title={isPaid ? "👑 Full Access Active · All 8 Mock Tests Unlocked" : "Free Demo Mode"}
                  onClick={() => setShowAccountMenu(!showAccountMenu)}
                >
                  <div className="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-extrabold text-xs flex items-center justify-center shadow-xs">
                    {(user.name || user.email || 'U').charAt(0).toUpperCase()}
                  </div>
                  {isPaid && (
                    <div className="absolute -top-1.5 -right-1.5 w-4 h-4 bg-amber-500 text-white rounded-full flex items-center justify-center shadow-xs border-2 border-white dark:border-slate-900">
                      <Crown className="w-2.5 h-2.5 fill-current" />
                    </div>
                  )}

                  {/* Hover tooltip for Crown / Access */}
                  <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 hidden group-hover:flex flex-col items-center z-50 pointer-events-none">
                    <div className="bg-slate-900 dark:bg-slate-100 text-white dark:text-slate-900 text-[10px] font-bold px-2.5 py-1 rounded-md shadow-xl whitespace-nowrap">
                      {isPaid ? "👑 Full Access Active" : "Free Demo Mode"}
                    </div>
                    <div className="w-2 h-2 bg-slate-900 dark:bg-slate-100 rotate-45 -mt-1" />
                  </div>
                </div>

                {/* Account / Signout Menu Toggle */}
                <div className="relative">
                  <button
                    onClick={() => setShowAccountMenu(!showAccountMenu)}
                    title="Account Options"
                    className="flex items-center gap-1 p-1 sm:p-1.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors cursor-pointer"
                  >
                    <ChevronDown className="w-3.5 h-3.5" />
                  </button>

                  {/* Dropdown Menu */}
                  {showAccountMenu && (
                    <div className="absolute right-0 mt-2 w-48 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-1.5 shadow-xl z-50 animate-in fade-in slide-in-from-top-2 duration-150">
                      <div className="px-3 py-2 border-b border-slate-100 dark:border-slate-800">
                        <div className="text-[10px] text-slate-400 font-semibold uppercase">Account</div>
                        <div className="text-xs font-bold text-slate-900 dark:text-white truncate">
                          {user.name || user.email}
                        </div>
                        {isPaid && (
                          <div className="text-[10px] text-amber-600 dark:text-amber-400 font-bold flex items-center gap-1 mt-0.5">
                            <Crown className="w-2.5 h-2.5" />
                            <span>Full Access Active</span>
                          </div>
                        )}
                      </div>

                      {isAdmin && (
                        <Link
                          to="/admin"
                          onClick={() => setShowAccountMenu(false)}
                          className="w-full flex items-center gap-2 px-3 py-2 text-xs font-semibold text-purple-700 dark:text-purple-300 hover:bg-purple-50 dark:hover:bg-purple-950/40 rounded-xl transition-colors cursor-pointer text-left border-b border-slate-100 dark:border-slate-800"
                        >
                          <Shield className="w-3.5 h-3.5 text-purple-600 dark:text-purple-400" />
                          <span>Admin Panel</span>
                        </Link>
                      )}
                      
                      <button
                        onClick={() => {
                          setShowAccountMenu(false);
                          setShowChangePwModal(true);
                        }}
                        className="w-full flex items-center gap-2 px-3 py-2 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 rounded-xl transition-colors cursor-pointer text-left"
                      >
                        <KeyRound className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400" />
                        <span>Change Password</span>
                      </button>

                      <button
                        onClick={() => {
                          setShowAccountMenu(false);
                          setShowSignOutConfirm(true);
                        }}
                        className="w-full flex items-center gap-2 px-3 py-2 text-xs font-semibold text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 rounded-xl transition-colors cursor-pointer text-left"
                      >
                        <LogOut className="w-3.5 h-3.5" />
                        <span>Sign Out</span>
                      </button>
                    </div>
                  )}
                </div>

              </div>
            ) : (
              <Link
                to="/login"
                className="flex items-center gap-1.5 bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold px-4 py-2 rounded-xl hover:bg-slate-800 dark:hover:bg-slate-100 transition-colors shadow-xs"
              >
                <LogIn className="w-3.5 h-3.5" />
                <span>Sign In</span>
              </Link>
            )}

          </div>

        </div>
      </header>

      {/* Change Password Modal */}
      <ChangePasswordModal
        isOpen={showChangePwModal}
        onClose={() => setShowChangePwModal(false)}
      />

      {/* Sign Out Confirmation Modal */}
      {showSignOutConfirm && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 max-w-sm w-full shadow-2xl text-center animate-in fade-in zoom-in-95 duration-150">
            <div className="w-12 h-12 bg-rose-50 dark:bg-rose-950/60 text-rose-600 rounded-2xl flex items-center justify-center mx-auto mb-3 border border-rose-200 dark:border-rose-800">
              <LogOut className="w-5 h-5" />
            </div>
            <h3 className="text-base font-bold text-slate-900 dark:text-white mb-1">Sign Out Confirmation</h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 mb-5 leading-relaxed">
              Are you sure you want to sign out? Your exam progress and test attempts are securely saved.
            </p>
            <div className="grid grid-cols-2 gap-2.5">
              <button
                onClick={() => setShowSignOutConfirm(false)}
                className="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 font-bold text-xs hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer"
              >
                Cancel
              </button>
              <button
                onClick={() => {
                  setShowSignOutConfirm(false);
                  logout();
                  navigate('/');
                }}
                className="px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs shadow-xs cursor-pointer"
              >
                Yes, Sign Out
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
