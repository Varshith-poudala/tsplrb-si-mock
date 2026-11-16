import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';

import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Exam from './pages/Exam';
import Login from './pages/Login';
import Admin from './pages/Admin';
import PaymentStatus from './pages/PaymentStatus';

export default function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <BrowserRouter>
          <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col transition-colors overflow-x-clip">
            <Navbar />
            <div className="flex-1 flex flex-col min-w-0">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/exam/:id" element={<Exam />} />
                <Route path="/login" element={<Login />} />
                <Route path="/admin" element={<Admin />} />
                <Route path="/payment/status" element={<PaymentStatus />} />
                <Route path="*" element={<Navigate to="/" replace />} />
              </Routes>
            </div>
          </div>
        </BrowserRouter>
      </AuthProvider>
    </ThemeProvider>
  );
}
