import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  X, ShieldCheck, Lock, CheckCircle2, AlertCircle, Loader2, 
  Smartphone, Mail, User as UserIcon, Sparkles, CreditCard 
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function CheckoutModal({ isOpen, onClose, onSuccess, targetTestId }) {
  const { user, refreshUser } = useAuth();
  const navigate = useNavigate();

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Sync with current user profile whenever modal opens or user updates
  useEffect(() => {
    if (isOpen) {
      setName(user?.name || '');
      setEmail(user?.email || '');
      // Format existing phone without prefix if present
      const existingPhone = (user?.phone || '').replace(/\D/g, '').replace(/^(91|0)/, '');
      setPhone(existingPhone);
      setError(null);
      setLoading(false);
    }
  }, [isOpen, user]);

  if (!isOpen) return null;

  // Clean phone input as user types: digits only, max 10
  const handlePhoneChange = (e) => {
    const raw = e.target.value.replace(/\D/g, '');
    // If user pastes +91..., strip 91
    const stripped = raw.length > 10 && raw.startsWith('91') ? raw.slice(2) : raw;
    setPhone(stripped.slice(0, 10));
    if (error) setError(null);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
    if (error) setError(null);
  };

  const handleProceed = async (e) => {
    e.preventDefault();
    setError(null);

    // 1. Validate Email
    const cleanEmail = email.trim().toLowerCase();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!cleanEmail || !emailRegex.test(cleanEmail)) {
      setError('Please enter a valid candidate email address for test activation & receipt.');
      return;
    }

    // 2. Validate 10-digit Indian Mobile Number
    const cleanPhone = phone.trim().replace(/\D/g, '');
    const phoneRegex = /^[6-9]\d{9}$/;
    if (!cleanPhone || !phoneRegex.test(cleanPhone)) {
      setError('Please enter a valid 10-digit Indian mobile number (e.g. 9876543210).');
      return;
    }

    setLoading(true);

    try {
      if (!window.Razorpay) {
        throw new Error('Razorpay SDK failed to load. Please check your internet connection and retry.');
      }

      // Step A: Create Order on backend with candidate's explicit email & phone
      const orderRes = await fetch('/api/payment/razorpay/create-order', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-user-email': cleanEmail,
        },
        body: JSON.stringify({
          email: cleanEmail,
          phone: cleanPhone,
          name: name.trim() || cleanEmail.split('@')[0],
        }),
      });

      const orderData = await orderRes.json();
      if (!orderRes.ok) {
        throw new Error(orderData.error || 'Failed to initiate secure order.');
      }

      // Step B: Launch Razorpay Checkout with STRICT prefill & readonly constraints
      // This completely prevents Razorpay from auto-filling previous users' device cookies!
      const candidateName = name.trim() || user?.name || cleanEmail.split('@')[0];
      const options = {
        key: orderData.keyId,
        amount: orderData.amount,
        currency: orderData.currency,
        name: 'TSPLRB SI Mock Test Series',
        description: 'Lifetime Access to All 8 Full 200-Question Exams',
        order_id: orderData.orderId,
        prefill: {
          name: candidateName,
          email: cleanEmail,
          contact: `+91${cleanPhone}`, // Explicit E.164 phone format
        },
        readonly: {
          email: true,   // Locks email to this candidate
          contact: true, // Locks phone to this candidate
        },
        theme: {
          color: '#0f172a',
        },
        handler: async function (response) {
          try {
            // Step C: Verify signature on backend
            const verifyRes = await fetch('/api/payment/razorpay/verify', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'x-user-email': cleanEmail,
              },
              body: JSON.stringify({
                razorpay_order_id: response.razorpay_order_id,
                razorpay_payment_id: response.razorpay_payment_id,
                razorpay_signature: response.razorpay_signature,
                userEmail: cleanEmail,
                phone: cleanPhone,
              }),
            });

            const verifyData = await verifyRes.json();
            if (verifyRes.ok && verifyData.success) {
              await refreshUser();
              onClose();
              if (onSuccess) {
                onSuccess(response.razorpay_payment_id);
              } else if (targetTestId) {
                navigate(`/exam/${targetTestId}`);
              } else {
                navigate('/payment/status?status=success&payment_id=' + response.razorpay_payment_id);
              }
            } else {
              throw new Error(verifyData.error || 'Payment verification failed');
            }
          } catch (verErr) {
            setError('Verification error: ' + verErr.message);
            setLoading(false);
          }
        },
        modal: {
          ondismiss: function () {
            setLoading(false);
          },
        },
      };

      const rzp = new window.Razorpay(options);
      rzp.on('payment.failed', function (resp) {
        setError(resp.error?.description || 'Payment was not completed. You can retry anytime.');
        setLoading(false);
      });

      rzp.open();
    } catch (err) {
      setError(err.message || 'Payment initiation failed.');
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-sm animate-fade-in">
      <div 
        className="relative w-full max-w-lg bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl shadow-2xl overflow-hidden animate-scale-in"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Top Header Bar */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-100 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-950/50">
          <div className="flex items-center gap-2">
            <span className="p-2 rounded-xl bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400 border border-blue-200 dark:border-blue-800">
              <ShieldCheck className="w-5 h-5" />
            </span>
            <div>
              <h2 className="text-sm font-bold text-slate-900 dark:text-white">Secure Checkout</h2>
              <p className="text-[11px] text-slate-500 dark:text-slate-400">TSPLRB SI 2026 Full Exam Series</p>
            </div>
          </div>
          <button
            onClick={onClose}
            disabled={loading}
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 max-h-[85vh] overflow-y-auto">
          
          {/* Plan Summary Card */}
          <div className="bg-gradient-to-br from-slate-900 to-slate-800 text-white p-5 rounded-2xl shadow-md mb-6 relative overflow-hidden">
            <div className="absolute top-0 right-0 -mt-2 -mr-2 w-24 h-24 bg-blue-500/10 rounded-full blur-xl pointer-events-none" />
            <div className="flex items-start justify-between">
              <div>
                <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30 uppercase tracking-wide mb-2">
                  <Sparkles className="w-3 h-3" />
                  All-Inclusive Package
                </span>
                <h3 className="text-base font-bold text-white">TSPLRB SI 2026 Test Series</h3>
                <p className="text-xs text-slate-300 mt-0.5">All 8 Full Exams • Lifetime Validity</p>
              </div>
              <div className="text-right">
                <div className="text-xs text-slate-400 line-through">₹499</div>
                <div className="text-2xl font-black text-white">₹99</div>
              </div>
            </div>

            {/* Checklist */}
            <div className="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-700/60 text-[11px] text-slate-300">
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 flex-shrink-0" />
                <span>All 8 Mock Tests (1,450 Qs)</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 flex-shrink-0" />
                <span>Bilingual (EN / తెలుగు)</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 flex-shrink-0" />
                <span>Official -0.20 Negative Mark</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 flex-shrink-0" />
                <span>Unlimited Retakes & Solutions</span>
              </div>
            </div>
          </div>

          {/* Form: Candidate Contact Details */}
          <form onSubmit={handleProceed} className="space-y-4">
            <div>
              <label className="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">
                Candidate Full Name
              </label>
              <div className="relative">
                <UserIcon className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Enter your name"
                  disabled={loading}
                  className="w-full pl-9 pr-3 py-2.5 text-xs bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-slate-900 dark:text-white"
                />
              </div>
            </div>

            {/* Email Field */}
            <div>
              <div className="flex items-center justify-between mb-1">
                <label className="block text-xs font-bold text-slate-700 dark:text-slate-300">
                  Email Address <span className="text-rose-500">*</span>
                </label>
                <span className="text-[10px] text-slate-400">Account will be activated on this email</span>
              </div>
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input
                  type="email"
                  required
                  value={email}
                  onChange={handleEmailChange}
                  placeholder="candidate@example.com"
                  disabled={loading}
                  className="w-full pl-9 pr-3 py-2.5 text-xs bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-slate-900 dark:text-white"
                />
              </div>
            </div>

            {/* Mobile Number Field */}
            <div>
              <div className="flex items-center justify-between mb-1">
                <label className="block text-xs font-bold text-slate-700 dark:text-slate-300">
                  Mobile Number <span className="text-rose-500">*</span>
                </label>
                <span className="text-[10px] text-slate-400">10-Digit WhatsApp / Call number</span>
              </div>
              <div className="relative flex items-center">
                <div className="absolute left-3 flex items-center gap-1.5 text-xs font-bold text-slate-600 dark:text-slate-400 border-r border-slate-200 dark:border-slate-700 pr-2">
                  <span>🇮🇳</span>
                  <span>+91</span>
                </div>
                <input
                  type="tel"
                  required
                  value={phone}
                  onChange={handlePhoneChange}
                  placeholder="9876543210"
                  maxLength={10}
                  disabled={loading}
                  className="w-full pl-20 pr-3 py-2.5 text-xs tracking-wider font-mono font-medium bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-slate-900 dark:text-white placeholder:text-slate-400"
                />
              </div>
              <p className="text-[10px] text-slate-400 dark:text-slate-500 mt-1">
                Used to lock your payment directly to your number and send payment receipts.
              </p>
            </div>

            {/* Error Feedback */}
            {error && (
              <div className="p-3 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-800 flex items-start gap-2.5 text-left text-xs text-rose-700 dark:text-rose-300">
                <AlertCircle className="w-4 h-4 text-rose-600 dark:text-rose-400 flex-shrink-0 mt-0.5" />
                <span className="text-[11px] leading-relaxed">{error}</span>
              </div>
            )}

            {/* Submit Action */}
            <div className="pt-2">
              <button
                type="submit"
                disabled={loading}
                className="w-full py-3 px-4 rounded-xl font-bold text-xs bg-blue-600 hover:bg-blue-700 text-white shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer disabled:opacity-70 disabled:cursor-not-allowed"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    <span>Opening Razorpay Gateway...</span>
                  </>
                ) : (
                  <>
                    <CreditCard className="w-4 h-4" />
                    <span>Proceed to Pay ₹99 via UPI / Cards</span>
                  </>
                )}
              </button>
            </div>

            {/* Razorpay Trust Footer */}
            <div className="text-center pt-2">
              <div className="inline-flex items-center gap-1.5 text-[10px] text-slate-400 dark:text-slate-500">
                <Lock className="w-3 h-3 text-emerald-500" />
                <span>256-bit Encrypted Checkout • Secured by Razorpay</span>
              </div>
            </div>
          </form>

        </div>
      </div>
    </div>
  );
}
