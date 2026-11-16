'use client';

import { useState, useEffect } from 'react';
import { useSession } from 'next-auth/react';
import Navbar from '@/components/Navbar';
import Link from 'next/link';
import { Crown, Shield, UserCheck, UserX, Search, PlusCircle, CheckCircle2, AlertCircle, RefreshCw, Mail, Users } from 'lucide-react';

export default function AdminPage() {
  const { data: session, status } = useSession();
  const [users, setUsers] = useState([]);
  const [stats, setStats] = useState({ totalUsers: 0, paidUsers: 0, adminGrants: 0, freeUsers: 0 });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchQuery, setSearchQuery] = useState('');

  // Quick grant form state
  const [targetEmail, setTargetEmail] = useState('');
  const [notes, setNotes] = useState('');
  const [granting, setGranting] = useState(false);
  const [actionMessage, setActionMessage] = useState({ text: '', type: '' });

  const fetchUsers = async () => {
    setLoading(true);
    setError('');
    try {
      const res = await fetch('/api/admin/users');
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || 'Failed to fetch admin data');
      }
      setUsers(data.users || []);
      setStats(data.stats || {});
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (session?.user?.role === 'admin') {
      fetchUsers();
    }
  }, [session]);

  const handleGrantAccess = async (email, isPaid, customNotes = '') => {
    setGranting(true);
    setActionMessage({ text: '', type: '' });
    try {
      const res = await fetch('/api/admin/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          isPaid,
          notes: customNotes || notes || 'Complimentary access granted by Admin',
        }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to update access');

      setActionMessage({ text: data.message, type: 'success' });
      setTargetEmail('');
      setNotes('');
      fetchUsers(); // Refresh list
    } catch (err) {
      setActionMessage({ text: err.message, type: 'error' });
    } finally {
      setGranting(false);
    }
  };

  if (status === 'loading') {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex items-center justify-center transition-colors">
        <div className="w-8 h-8 border-3 border-blue-600 border-t-transparent rounded-full animate-spin"></div>
      </div>
    );
  }

  const isAdmin = session?.user?.role === 'admin';

  if (!isAdmin) {
    return (
      <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-white flex flex-col transition-colors">
        <Navbar />
        <div className="flex-1 flex items-center justify-center p-4">
          <div className="max-w-md w-full bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl p-8 text-center shadow-lg">
            <div className="w-12 h-12 bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 rounded-xl flex items-center justify-center mx-auto mb-4 border border-rose-200 dark:border-rose-800">
              <AlertCircle className="w-6 h-6" />
            </div>
            <h1 className="text-xl font-bold text-slate-900 dark:text-white mb-2">Admin Portal Restricted</h1>
            <p className="text-xs text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
              You must be signed in as the authorized Super Admin (<span className="text-blue-600 dark:text-amber-400 font-mono">varshithpoudala@gmail.com</span>) to manage student access.
            </p>
            <Link
              href="/login"
              className="inline-block w-full bg-slate-900 dark:bg-white text-white dark:text-slate-900 font-semibold py-2.5 rounded-xl transition-colors text-xs"
            >
              Sign In as Admin
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const filteredUsers = users.filter(u =>
    u.email.toLowerCase().includes(searchQuery.toLowerCase()) ||
    (u.name && u.name.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col transition-colors">
      <Navbar />

      <main className="flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-8">
        
        {/* Header */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pb-6 border-b border-slate-200 dark:border-slate-800">
          <div>
            <div className="flex items-center gap-2">
              <span className="bg-purple-100 dark:bg-purple-950/60 text-purple-800 dark:text-purple-300 text-xs font-semibold px-2 py-0.5 rounded-full border border-purple-200 dark:border-purple-800">
                Super Admin
              </span>
              <h1 className="text-2xl font-bold text-slate-900 dark:text-white">Platform Administration</h1>
            </div>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
              Signed in as: <span className="font-semibold text-slate-900 dark:text-white">{session.user.email}</span>. Grant free access to any student email.
            </p>
          </div>

          <button
            onClick={fetchUsers}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-white dark:bg-slate-800 hover:bg-slate-50 text-slate-700 dark:text-slate-200 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 transition-colors shadow-xs cursor-pointer"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
            <span>Refresh</span>
          </button>
        </div>

        {/* Action Message Banner */}
        {actionMessage.text && (
          <div
            className={`mt-6 p-4 rounded-xl flex items-center gap-3 text-xs font-medium border ${
              actionMessage.type === 'success'
                ? 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300'
                : 'bg-rose-50 dark:bg-rose-950/40 border-rose-200 dark:border-rose-800 text-rose-800 dark:text-rose-300'
            }`}
          >
            {actionMessage.type === 'success' ? (
              <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400 flex-shrink-0" />
            ) : (
              <AlertCircle className="w-4 h-4 text-rose-600 dark:text-rose-400 flex-shrink-0" />
            )}
            <span>{actionMessage.text}</span>
          </div>
        )}

        {/* Stats Grid */}
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
              <Users className="w-3.5 h-3.5 text-blue-600 dark:text-blue-400" />
              Total Candidates
            </div>
            <div className="text-2xl font-bold text-slate-900 dark:text-white mt-1.5">{stats.totalUsers || 0}</div>
          </div>

          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
              <Crown className="w-3.5 h-3.5 text-amber-500" />
              Total Full Access
            </div>
            <div className="text-2xl font-bold text-slate-900 dark:text-amber-400 mt-1.5">{stats.paidUsers || 0}</div>
          </div>

          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
              <UserCheck className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
              Admin Grants
            </div>
            <div className="text-2xl font-bold text-emerald-600 dark:text-emerald-400 mt-1.5">{stats.adminGrants || 0}</div>
          </div>

          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-4 shadow-xs">
            <div className="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
              <Shield className="w-3.5 h-3.5 text-slate-400" />
              Free Demo Tier
            </div>
            <div className="text-2xl font-bold text-slate-700 dark:text-slate-300 mt-1.5">{stats.freeUsers || 0}</div>
          </div>
        </div>

        {/* Quick Grant Box */}
        <div className="mt-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-5 sm:p-6 shadow-xs">
          <div className="flex items-center gap-2 mb-1.5">
            <PlusCircle className="w-4 h-4 text-purple-600 dark:text-purple-400" />
            <h2 className="text-sm font-bold text-slate-900 dark:text-white">Grant Free Access to Any Email</h2>
          </div>
          <p className="text-xs text-slate-500 dark:text-slate-400 mb-4">
            Enter candidate's email address. They will be granted instant full access to all 200-question exams for free.
          </p>

          <form
            onSubmit={(e) => {
              e.preventDefault();
              if (targetEmail) handleGrantAccess(targetEmail, true);
            }}
            className="flex flex-col sm:flex-row gap-2.5"
          >
            <div className="flex-1 relative">
              <Mail className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="email"
                placeholder="candidate.email@gmail.com"
                value={targetEmail}
                onChange={(e) => setTargetEmail(e.target.value)}
                required
                className="w-full bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-750 rounded-lg pl-9 pr-3 py-2 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-blue-600"
              />
            </div>

            <input
              type="text"
              placeholder="Notes (e.g. WhatsApp request)"
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              className="sm:w-60 bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-750 rounded-lg px-3 py-2 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-blue-600"
            />

            <button
              type="submit"
              disabled={granting || !targetEmail}
              className="bg-emerald-600 hover:bg-emerald-700 disabled:opacity-50 text-white font-bold px-4 py-2 rounded-lg text-xs flex items-center justify-center gap-1.5 transition-colors shadow-xs cursor-pointer"
            >
              <UserCheck className="w-3.5 h-3.5" />
              <span>{granting ? 'Granting...' : 'Grant Access'}</span>
            </button>
          </form>
        </div>

        {/* User Management Table */}
        <div className="mt-8 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl overflow-hidden shadow-xs">
          <div className="p-4 sm:p-5 border-b border-slate-100 dark:border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
            <div>
              <h2 className="text-sm font-bold text-slate-900 dark:text-white">Registered Candidates & Permissions</h2>
              <p className="text-xs text-slate-500 dark:text-slate-400">Total {users.length} registered candidates</p>
            </div>

            <div className="w-full sm:w-60 relative">
              <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                placeholder="Search candidates..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-750 rounded-lg pl-8 pr-3 py-1.5 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:border-blue-600"
              />
            </div>
          </div>

          {loading ? (
            <div className="p-12 text-center text-slate-500">
              <div className="w-6 h-6 border-2 border-blue-600 border-t-transparent rounded-full animate-spin mx-auto mb-2"></div>
              Loading candidates...
            </div>
          ) : filteredUsers.length === 0 ? (
            <div className="p-12 text-center text-slate-500 text-xs">
              No candidates found matching your search.
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-slate-700 dark:text-slate-300">
                <thead className="bg-slate-50 dark:bg-slate-950/60 text-slate-500 dark:text-slate-400 uppercase text-[10px] tracking-wider border-b border-slate-200 dark:border-slate-800">
                  <tr>
                    <th className="py-3 px-4">Candidate</th>
                    <th className="py-3 px-4">Role</th>
                    <th className="py-3 px-4">Access Status</th>
                    <th className="py-3 px-4">Grant Method</th>
                    <th className="py-3 px-4">Attempts</th>
                    <th className="py-3 px-4 text-right">Actions</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100 dark:divide-slate-800">
                  {filteredUsers.map((u) => {
                    const isCandidatePaid = u.isPaid || u.role === 'admin';
                    return (
                      <tr key={u._id || u.email} className="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition-colors">
                        <td className="py-3 px-4">
                          <div className="font-semibold text-slate-900 dark:text-white">{u.name || 'Candidate'}</div>
                          <div className="text-[11px] text-slate-500 dark:text-slate-400 font-mono">{u.email}</div>
                          {u.notes && <div className="text-[10px] text-amber-700 dark:text-amber-300 mt-0.5">{u.notes}</div>}
                        </td>
                        <td className="py-3 px-4">
                          {u.role === 'admin' ? (
                            <span className="bg-purple-100 dark:bg-purple-900/40 text-purple-800 dark:text-purple-300 border border-purple-200 dark:border-purple-700/50 px-2 py-0.5 rounded text-[10px] font-bold">
                              ADMIN
                            </span>
                          ) : (
                            <span className="text-slate-500">Candidate</span>
                          )}
                        </td>
                        <td className="py-3 px-4">
                          {isCandidatePaid ? (
                            <span className="inline-flex items-center gap-1 bg-emerald-50 dark:bg-emerald-950 border border-emerald-200 dark:border-emerald-700 text-emerald-800 dark:text-emerald-300 px-2 py-0.5 rounded text-[10px] font-bold">
                              <CheckCircle2 className="w-3 h-3" />
                              Full Access
                            </span>
                          ) : u.notes?.includes('UTR') ? (
                            <span className="inline-flex items-center gap-1 bg-amber-50 dark:bg-amber-950 border border-amber-200 dark:border-amber-600 text-amber-800 dark:text-amber-300 px-2 py-0.5 rounded text-[10px] font-bold animate-pulse">
                              Pending UTR Review
                            </span>
                          ) : (
                            <span className="inline-flex items-center gap-1 bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 px-2 py-0.5 rounded text-[10px]">
                              Free Demo Only
                            </span>
                          )}
                        </td>
                        <td className="py-3 px-4 text-slate-500 dark:text-slate-400">
                          {u.accessGrantedBy === 'admin' ? (
                            <span className="text-purple-700 dark:text-purple-300 font-medium">Free Admin Grant</span>
                          ) : u.accessGrantedBy === 'payment' ? (
                            <span className="text-emerald-700 dark:text-emerald-400 font-medium">Paid (₹99)</span>
                          ) : (
                            <span>—</span>
                          )}
                        </td>
                        <td className="py-3 px-4 font-bold text-slate-800 dark:text-slate-200">
                          {u.attemptsCount || 0}
                        </td>
                        <td className="py-3 px-4 text-right">
                          {u.role !== 'admin' && (
                            <div>
                              {isCandidatePaid ? (
                                <button
                                  onClick={() => handleGrantAccess(u.email, false, 'Revoked by admin')}
                                  className="text-rose-600 hover:text-rose-700 hover:bg-rose-50 dark:text-rose-400 dark:hover:bg-rose-950/40 px-2.5 py-1 rounded border border-rose-200 dark:border-rose-900/60 text-[11px] font-medium transition-colors cursor-pointer"
                                >
                                  Revoke Access
                                </button>
                              ) : (
                                <button
                                  onClick={() => handleGrantAccess(u.email, true, 'Granted via Admin Panel')}
                                  className="bg-emerald-600 hover:bg-emerald-700 text-white px-2.5 py-1 rounded text-[11px] font-bold transition-colors shadow-xs cursor-pointer"
                                >
                                  Grant Free Access
                                </button>
                              )}
                            </div>
                          )}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )}
        </div>

      </main>
    </div>
  );
}
