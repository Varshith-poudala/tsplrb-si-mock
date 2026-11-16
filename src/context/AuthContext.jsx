import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import { clearLegacyUnscopedProgress } from '../utils/storage';

const AuthContext = createContext({
  user: null,
  loading: true,
  login: async () => {},
  register: async () => {},
  logout: () => {},
  changePassword: async () => {},
  forgotPassword: async () => {},
  resetPassword: async () => {},
  refreshUser: async () => {},
});

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Load stored user on mount and sync with database
  useEffect(() => {
    async function initAuth() {
      try {
        clearLegacyUnscopedProgress();
        const stored = localStorage.getItem('tsplrb_user');
        if (stored) {
          const parsed = JSON.parse(stored);
          setUser(parsed);

          // Verify fresh status from server (e.g. check if isPaid was updated)
          const res = await fetch('/api/auth/me', {
            headers: { 'x-user-email': parsed.email },
          });
          if (res.ok) {
            const data = await res.json();
            if (data.user) {
              setUser(data.user);
              localStorage.setItem('tsplrb_user', JSON.stringify(data.user));
            }
          }
        }
      } catch (err) {
        console.error('Failed to initialize user session:', err);
      } finally {
        setLoading(false);
      }
    }
    initAuth();
  }, []);

  const login = useCallback(async (email, password) => {
    try {
      clearLegacyUnscopedProgress();
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Login failed');

      setUser(data.user);
      localStorage.setItem('tsplrb_user', JSON.stringify(data.user));
      return { success: true, user: data.user };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }, []);

  const register = useCallback(async (email, name, password) => {
    try {
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, name, password }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Registration failed');

      setUser(data.user);
      localStorage.setItem('tsplrb_user', JSON.stringify(data.user));
      return { success: true, user: data.user };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }, []);

  const changePassword = useCallback(async (currentPassword, newPassword) => {
    if (!user?.email) return { success: false, error: 'Not authenticated' };
    try {
      const res = await fetch('/api/auth/change-password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-user-email': user.email,
        },
        body: JSON.stringify({
          email: user.email,
          currentPassword,
          newPassword,
        }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to change password');
      return { success: true, message: data.message };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }, [user]);

  const forgotPassword = useCallback(async (email) => {
    try {
      const res = await fetch('/api/auth/forgot-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to request reset code');
      return { success: true, resetCode: data.resetCode, message: data.message };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }, []);

  const resetPassword = useCallback(async (email, resetCode, newPassword) => {
    try {
      const res = await fetch('/api/auth/reset-password', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, resetCode, newPassword }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to reset password');
      return { success: true, message: data.message };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }, []);

  const logout = useCallback(() => {
    setUser(null);
    localStorage.removeItem('tsplrb_user');
    clearLegacyUnscopedProgress();
  }, []);

  const refreshUser = useCallback(async () => {
    if (!user?.email) return;
    try {
      const res = await fetch('/api/auth/me', {
        headers: { 'x-user-email': user.email },
      });
      if (res.ok) {
        const data = await res.json();
        if (data.user) {
          setUser(data.user);
          localStorage.setItem('tsplrb_user', JSON.stringify(data.user));
        }
      }
    } catch (err) {
      console.warn('refreshUser error:', err);
    }
  }, [user]);

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        login,
        register,
        logout,
        changePassword,
        forgotPassword,
        resetPassword,
        refreshUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
