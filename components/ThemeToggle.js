'use client';

import { useTheme } from './ThemeProvider';
import { Sun, Moon } from 'lucide-react';

export default function ThemeToggle({ className = '', showLabel = false }) {
  const { theme, toggleTheme, mounted } = useTheme();

  return (
    <button
      onClick={toggleTheme}
      type="button"
      className={`inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors shadow-sm text-xs font-medium cursor-pointer ${className}`}
      aria-label="Toggle light or dark theme"
      title={mounted && theme === 'dark' ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
    >
      {mounted && theme === 'dark' ? (
        <>
          <Sun className="w-3.5 h-3.5 text-amber-400" />
          {showLabel && <span>Light Mode</span>}
        </>
      ) : (
        <>
          <Moon className="w-3.5 h-3.5 text-slate-600 dark:text-slate-400" />
          {showLabel && <span>Dark Mode</span>}
        </>
      )}
    </button>
  );
}
