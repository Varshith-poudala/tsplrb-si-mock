import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
  Shield, Crown, CheckCircle2, XCircle, Search, UserPlus, RefreshCw, 
  BookOpen, PlusCircle, Clock, ArrowRight, Layers, FileText, Check, AlertCircle, X, ChevronRight
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function Admin() {
  const { user, loading: authLoading } = useAuth();
  
  // Navigation Tabs
  const [activeTab, setActiveTab] = useState('users'); // 'users' | 'tests'

  // Users State
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [targetEmail, setTargetEmail] = useState('');
  const [statusMsg, setStatusMsg] = useState(null);

  // Tests State
  const [tests, setTests] = useState([]);
  const [testsLoading, setTestsLoading] = useState(false);
  const [showCreateTestModal, setShowCreateTestModal] = useState(false);
  const [createLoading, setCreateLoading] = useState(false);
  const [createError, setCreateError] = useState(null);

  // Create Test Form State
  const [formData, setFormData] = useState({
    title: '',
    title_te: '',
    testId: '',
    difficulty: 'Medium',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: '',
  });

  const isAdmin = user?.role === 'admin' && user?.email?.toLowerCase().trim() === 'varshithpoudala@gmail.com';

  const loadUsers = async () => {
    if (!user?.email) return;
    setLoading(true);
    try {
      const res = await fetch('/api/admin/users', {
        headers: { 'x-user-email': user.email },
      });
      const data = await res.json();
      if (res.ok) setUsers(data.users || []);
    } catch (err) {
      console.error('Failed to load users:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadTests = async () => {
    if (!user?.email) return;
    setTestsLoading(true);
    try {
      const res = await fetch('/api/admin/tests', {
        headers: { 'x-user-email': user.email },
      });
      const data = await res.json();
      if (res.ok) setTests(data.tests || []);
    } catch (err) {
      console.error('Failed to load tests:', err);
    } finally {
      setTestsLoading(false);
    }
  };

  useEffect(() => {
    if (isAdmin && user?.email) {
      loadUsers();
      loadTests();
    }
  }, [isAdmin, user?.email]);

  const handleToggleAccess = async (targetUserEmail, currentPaidStatus) => {
    try {
      const res = await fetch('/api/admin/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-user-email': user.email,
        },
        body: JSON.stringify({
          email: targetUserEmail,
          isPaid: !currentPaidStatus,
        }),
      });
      if (res.ok) {
        setStatusMsg(`Updated access for ${targetUserEmail}`);
        loadUsers();
        setTimeout(() => setStatusMsg(null), 3000);
      }
    } catch (e) {
      alert('Error updating user access');
    }
  };

  const handleGrantCustom = async (e) => {
    e.preventDefault();
    if (!targetEmail) return;
    await handleToggleAccess(targetEmail, false);
    setTargetEmail('');
  };

  const handleCreateTestSubmit = async (e) => {
    e.preventDefault();
    setCreateError(null);
    setCreateLoading(true);

    try {
      const res = await fetch('/api/admin/tests', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-user-email': user.email,
        },
        body: JSON.stringify(formData),
      });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || 'Failed to create test');
      }

      setStatusMsg(data.message || 'Mock test created successfully!');
      setShowCreateTestModal(false);
      // Reset form
      setFormData({
        title: '',
        title_te: '',
        testId: '',
        difficulty: 'Medium',
        totalQuestions: 200,
        totalMarks: 200,
        durationMinutes: 180,
        negativeMarking: 0.20,
        isFreeDemo: false,
        description: '',
      });
      loadTests();
      setTimeout(() => setStatusMsg(null), 4000);
    } catch (err) {
      setCreateError(err.message);
    } finally {
      setCreateLoading(false);
    }
  };

  if (authLoading) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center">
        <div className="w-8 h-8 border-3 border-purple-600 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  if (!isAdmin) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-4">
        <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-8 text-center shadow-sm">
          <div className="w-12 h-12 bg-rose-50 text-rose-600 rounded-2xl flex items-center justify-center mx-auto mb-3">
            <Shield className="w-6 h-6" />
          </div>
          <h1 className="text-xl font-bold mb-2 text-slate-900 dark:text-white">Access Restricted</h1>
          <p className="text-xs text-slate-500 mb-6">
            This administration portal is reserved for authorized system administrators.
          </p>
          <Link
            to="/dashboard"
            className="inline-block bg-slate-900 dark:bg-white text-white dark:text-slate-900 text-xs font-bold px-6 py-2.5 rounded-xl cursor-pointer"
          >
            Back to Dashboard
          </Link>
        </div>
      </div>
    );
  }

  const filteredUsers = users.filter(u => 
    (u.email || '').toLowerCase().includes(searchTerm.toLowerCase()) ||
    (u.name || '').toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <main className="max-w-[1440px] mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="text-xs font-bold text-purple-600 dark:text-purple-400 uppercase tracking-wider flex items-center gap-1">
              <Crown className="w-3.5 h-3.5" />
              <span>Super Admin Dashboard • Varshith Poudala</span>
            </span>
          </div>
          <h1 className="text-2xl font-bold text-slate-900 dark:text-white">System Administration & Test Hub</h1>
          <p className="text-xs text-slate-500">Manage candidate accounts, create mock papers, and monitor live test papers</p>
        </div>

        <div className="flex items-center gap-2">
          {activeTab === 'tests' && (
            <button
              onClick={() => setShowCreateTestModal(true)}
              className="flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white px-3.5 py-2 rounded-xl text-xs font-bold cursor-pointer shadow-xs"
            >
              <PlusCircle className="w-3.5 h-3.5" />
              <span>Create New Test</span>
            </button>
          )}

          <button
            onClick={() => {
              loadUsers();
              loadTests();
            }}
            className="flex items-center gap-1.5 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 px-3.5 py-2 rounded-xl text-xs font-semibold cursor-pointer"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${loading || testsLoading ? 'animate-spin' : ''}`} />
            <span>Refresh</span>
          </button>
        </div>
      </div>

      {statusMsg && (
        <div className="mb-4 p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300 text-xs font-semibold flex items-center gap-2">
          <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
          <span>{statusMsg}</span>
        </div>
      )}

      {/* Tabs Switcher */}
      <div className="flex items-center gap-2 mb-6 border-b border-slate-200 dark:border-slate-800 pb-2">
        <button
          onClick={() => setActiveTab('users')}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
            activeTab === 'users'
              ? 'bg-purple-600 text-white shadow-sm'
              : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
          }`}
        >
          <Crown className="w-3.5 h-3.5" />
          <span>Candidate Users & Access ({users.length})</span>
        </button>

        <button
          onClick={() => setActiveTab('tests')}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
            activeTab === 'tests'
              ? 'bg-purple-600 text-white shadow-sm'
              : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800'
          }`}
        >
          <BookOpen className="w-3.5 h-3.5" />
          <span>Mock Test Papers ({tests.length})</span>
        </button>
      </div>

      {/* TAB 1: USERS MANAGEMENT */}
      {activeTab === 'users' && (
        <div>
          {/* Manual Grant Input */}
          <form onSubmit={handleGrantCustom} className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-4 mb-6 flex flex-col sm:flex-row items-center gap-3">
            <div className="flex-1 w-full">
              <input
                type="email"
                value={targetEmail}
                onChange={(e) => setTargetEmail(e.target.value)}
                placeholder="Enter candidate email to grant instant full access..."
                className="w-full px-3.5 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-xs text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <button
              type="submit"
              className="w-full sm:w-auto bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-4 py-2 rounded-xl flex items-center justify-center gap-1.5 cursor-pointer whitespace-nowrap shadow-xs"
            >
              <UserPlus className="w-3.5 h-3.5" />
              <span>Grant Access</span>
            </button>
          </form>

          {/* Users Table */}
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl overflow-hidden shadow-xs">
            <div className="p-4 border-b border-slate-100 dark:border-slate-800 flex items-center justify-between gap-4">
              <div className="relative flex-1 max-w-xs">
                <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                <input
                  type="text"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  placeholder="Search candidate email or name..."
                  className="w-full pl-8 pr-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-800 text-xs bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                />
              </div>
              <span className="text-xs text-slate-400 font-semibold">{filteredUsers.length} Users Found</span>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-slate-700 dark:text-slate-300">
                <thead className="bg-slate-50 dark:bg-slate-950/60 text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-200 dark:border-slate-800">
                  <tr>
                    <th className="py-3 px-4">Candidate</th>
                    <th className="py-3 px-4">Role</th>
                    <th className="py-3 px-4">Access Status</th>
                    <th className="py-3 px-4">Mobile</th>
                    <th className="py-3 px-4">Granted Method</th>
                    <th className="py-3 px-4 text-right">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 dark:divide-slate-800">
                  {filteredUsers.map((u) => {
                    const isUserPaid = u.isPaid || u.role === 'admin';
                    return (
                      <tr key={u._id} className="hover:bg-slate-50 dark:hover:bg-slate-800/40">
                        <td className="py-3.5 px-4">
                          <div className="font-bold text-slate-900 dark:text-white">{u.name || 'Candidate'}</div>
                          <div className="text-[11px] text-slate-400">{u.email}</div>
                        </td>
                        <td className="py-3.5 px-4">
                          <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                            u.role === 'admin'
                              ? 'bg-purple-50 dark:bg-purple-950 text-purple-700 dark:text-purple-300 border border-purple-200 dark:border-purple-800'
                              : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                          }`}>
                            {u.role || 'user'}
                          </span>
                        </td>
                        <td className="py-3.5 px-4">
                          {isUserPaid ? (
                            <span className="inline-flex items-center gap-1 text-emerald-600 dark:text-emerald-400 font-bold">
                              <CheckCircle2 className="w-3.5 h-3.5" />
                              <span>Full Access (₹99)</span>
                            </span>
                          ) : (
                            <span className="inline-flex items-center gap-1 text-slate-400 font-medium">
                              <XCircle className="w-3.5 h-3.5" />
                              <span>Demo Only</span>
                            </span>
                          )}
                        </td>
                        <td className="py-3.5 px-4 font-mono text-[11px] text-slate-500">
                          {u.phone ? `+91 ${u.phone}` : '—'}
                        </td>
                        <td className="py-3.5 px-4 text-slate-400">
                          {u.accessGrantedBy || 'none'}
                        </td>
                        <td className="py-3.5 px-4 text-right">
                          {u.role !== 'admin' && (
                            <button
                              onClick={() => handleToggleAccess(u.email, isUserPaid)}
                              className={`px-3 py-1 rounded-lg text-[11px] font-bold cursor-pointer transition-colors ${
                                isUserPaid
                                  ? 'bg-rose-50 hover:bg-rose-100 text-rose-700 dark:bg-rose-950 dark:text-rose-300 border border-rose-200 dark:border-rose-800'
                                  : 'bg-emerald-50 hover:bg-emerald-100 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800'
                              }`}
                            >
                              {isUserPaid ? 'Revoke Access' : 'Grant Full Access'}
                            </button>
                          )}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: MOCK TEST PAPERS MANAGEMENT */}
      {activeTab === 'tests' && (
        <div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {tests.map((test) => (
              <div 
                key={test.testId}
                className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-5 shadow-xs flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${
                      test.difficulty === 'Easy'
                        ? 'bg-emerald-50 text-emerald-600 dark:bg-emerald-950/60 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800'
                        : test.difficulty === 'Hard'
                        ? 'bg-rose-50 text-rose-600 dark:bg-rose-950/60 dark:text-rose-400 border border-rose-200 dark:border-rose-800'
                        : 'bg-blue-50 text-blue-600 dark:bg-blue-950/60 dark:text-blue-400 border border-blue-200 dark:border-blue-800'
                    }`}>
                      {test.difficulty}
                    </span>

                    <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                      test.isFreeDemo
                        ? 'bg-amber-50 text-amber-600 dark:bg-amber-950/60 dark:text-amber-400'
                        : 'bg-purple-50 text-purple-600 dark:bg-purple-950/60 dark:text-purple-400'
                    }`}>
                      {test.isFreeDemo ? 'Free Demo' : 'Full Paper (₹99)'}
                    </span>
                  </div>

                  <h3 className="font-bold text-sm text-slate-900 dark:text-white leading-snug">
                    {test.title}
                  </h3>
                  {test.title_te && (
                    <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-1 line-clamp-1 font-serif">
                      {test.title_te}
                    </p>
                  )}

                  <div className="flex items-center gap-3 mt-4 text-[11px] text-slate-500 dark:text-slate-400 font-medium">
                    <span className="flex items-center gap-1">
                      <Layers className="w-3.5 h-3.5 text-blue-500" />
                      <span>{test.totalQuestions} Questions</span>
                    </span>
                    <span className="flex items-center gap-1">
                      <Clock className="w-3.5 h-3.5 text-emerald-500" />
                      <span>{test.durationMinutes} Mins</span>
                    </span>
                    <span>• {test.totalMarks} Marks</span>
                  </div>

                  <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-2 line-clamp-2">
                    {test.description}
                  </p>
                </div>

                <div className="pt-4 mt-4 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
                  <span className="text-[10px] font-mono text-slate-400 truncate max-w-[150px]">
                    {test.testId}
                  </span>
                  <Link
                    to={`/exam/${test.testId}`}
                    target="_blank"
                    className="flex items-center gap-1 text-xs font-bold text-blue-600 dark:text-blue-400 hover:text-blue-700"
                  >
                    <span>Launch Exam</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* CREATE NEW TEST MODAL */}
      {showCreateTestModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-sm animate-fade-in">
          <div className="relative w-full max-w-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl shadow-2xl overflow-hidden p-6 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between pb-4 border-b border-slate-100 dark:border-slate-800 mb-4">
              <div className="flex items-center gap-2">
                <span className="p-2 rounded-xl bg-purple-50 dark:bg-purple-950 text-purple-600 dark:text-purple-400">
                  <PlusCircle className="w-5 h-5" />
                </span>
                <div>
                  <h2 className="text-base font-bold text-slate-900 dark:text-white">Create New Mock Test</h2>
                  <p className="text-[11px] text-slate-500">Configure and register a new simulated question paper</p>
                </div>
              </div>
              <button
                onClick={() => setShowCreateTestModal(false)}
                className="text-slate-400 hover:text-slate-600 cursor-pointer p-1"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {createError && (
              <div className="mb-4 p-3 rounded-xl bg-rose-50 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-xs flex items-center gap-2">
                <AlertCircle className="w-4 h-4 flex-shrink-0" />
                <span>{createError}</span>
              </div>
            )}

            <form onSubmit={handleCreateTestSubmit} className="space-y-4 text-xs">
              <div>
                <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
                  Test Title (English) *
                </label>
                <input
                  type="text"
                  required
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                  placeholder="e.g. TSPLRB SI Mock Test 9 (Advanced Revision 200 Qs)"
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                />
              </div>

              <div>
                <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
                  Test Title (Telugu)
                </label>
                <input
                  type="text"
                  value={formData.title_te}
                  onChange={(e) => setFormData({ ...formData, title_te: e.target.value })}
                  placeholder="తెలంగాణ ఎస్సై మాక్ టెస్ట్ 9"
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
                    Difficulty Level
                  </label>
                  <select
                    value={formData.difficulty}
                    onChange={(e) => setFormData({ ...formData, difficulty: e.target.value })}
                    className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                  >
                    <option value="Easy">Easy (సులభం)</option>
                    <option value="Medium">Medium (మధ్యస్థం)</option>
                    <option value="Hard">Hard (కఠినం)</option>
                  </select>
                </div>

                <div>
                  <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
                    Total Questions
                  </label>
                  <input
                    type="number"
                    value={formData.totalQuestions}
                    onChange={(e) => setFormData({ ...formData, totalQuestions: Number(e.target.value), totalMarks: Number(e.target.value) })}
                    className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
                    Duration (Minutes)
                  </label>
                  <input
                    type="number"
                    value={formData.durationMinutes}
                    onChange={(e) => setFormData({ ...formData, durationMinutes: Number(e.target.value) })}
                    className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                  />
                </div>

                <div>
                  <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
                    Negative Marking
                  </label>
                  <input
                    type="number"
                    step="0.05"
                    value={formData.negativeMarking}
                    onChange={(e) => setFormData({ ...formData, negativeMarking: Number(e.target.value) })}
                    className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                  />
                </div>
              </div>

              <div>
                <label className="block font-bold text-slate-700 dark:text-slate-300 mb-1">
                  Description
                </label>
                <textarea
                  rows={2}
                  value={formData.description}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                  placeholder="Summary of topics covered, difficulty calibration, and syllabus focus..."
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white"
                />
              </div>

              <div className="pt-2">
                <button
                  type="submit"
                  disabled={createLoading}
                  className="w-full py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-xl transition-all shadow-md flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-60"
                >
                  {createLoading ? 'Publishing Mock Test...' : 'Publish Mock Test to Catalog'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

    </main>
  );
}
