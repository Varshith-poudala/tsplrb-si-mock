import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import mongoose from 'mongoose';

// Load environment variables from .env.local
dotenv.config({ path: '.env.local' });

import connectToDatabase from '../lib/mongodb.js';
import User from '../models/User.js';
import Attempt from '../models/Attempt.js';
import Payment from '../models/Payment.js';
import Question from '../models/Question.js';
import { hashPassword, verifyPassword } from '../lib/crypto-auth.js';
import { sendPasswordResetEmail, isEmailConfigured } from '../lib/mailer.js';

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Helper to determine whether an email belongs to the sole system Super Admin
function isUserAdmin(email) {
  if (!email) return false;
  const clean = String(email).toLowerCase().trim();
  const rawAdminList = (process.env.ADMIN_EMAILS || 'varshithpoudala@gmail.com')
    .toLowerCase()
    .split(',')
    .map(e => e.trim());
  return rawAdminList.includes(clean);
}

// Helper to extract authenticated user from request header (x-user-email)
async function getAuthUser(req) {
  const emailHeader = req.headers['x-user-email'] || req.query.userEmail;
  if (!emailHeader) return null;
  const email = String(emailHeader).toLowerCase().trim();
  const isAdmin = isUserAdmin(email);

  try {
    await connectToDatabase();
    let dbUser = await User.findOne({ email });
    if (!dbUser) {
      dbUser = await User.create({
        email,
        name: email.split('@')[0],
        role: isAdmin ? 'admin' : 'user',
        isPaid: isAdmin,
        accessGrantedBy: isAdmin ? 'admin' : null,
        accessGrantedAt: isAdmin ? new Date() : null,
      });
    } else if (isAdmin && (!dbUser.isPaid || dbUser.role !== 'admin')) {
      dbUser.role = 'admin';
      dbUser.isPaid = true;
      await dbUser.save();
    } else if (!isAdmin && dbUser.role === 'admin') {
      // Security: demote any non-super-admin user back to standard 'user'
      dbUser.role = 'user';
      await dbUser.save();
    }
    return dbUser;
  } catch (err) {
    console.error('getAuthUser error:', err);
    return { email, role: isAdmin ? 'admin' : 'user', isPaid: isAdmin };
  }
}

// ----------------------------------------------------
// 1. HEALTH CHECK
// ----------------------------------------------------
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', server: 'express', timestamp: new Date().toISOString() });
});

// ----------------------------------------------------
// 2. AUTHENTICATION ROUTES (REGISTER, LOGIN, CHANGE PW, FORGOT PW)
// ----------------------------------------------------
app.post('/api/auth/register', async (req, res) => {
  try {
    const { email, name, password } = req.body;
    if (!email || !password) {
      return res.status(400).json({ error: 'Email and password are required' });
    }
    if (password.length < 6) {
      return res.status(400).json({ error: 'Password must be at least 6 characters' });
    }

    const cleanEmail = email.toLowerCase().trim();
    await connectToDatabase();

    const existing = await User.findOne({ email: cleanEmail });
    if (existing) {
      return res.status(400).json({ error: 'An account with this email already exists. Please sign in.' });
    }

    const isAdmin = isUserAdmin(cleanEmail);

    const { hash, salt } = hashPassword(password);

    const newUser = await User.create({
      email: cleanEmail,
      name: name || cleanEmail.split('@')[0],
      passwordHash: hash,
      salt: salt,
      role: isAdmin ? 'admin' : 'user',
      isPaid: isAdmin,
      accessGrantedBy: isAdmin ? 'admin' : null,
      accessGrantedAt: isAdmin ? new Date() : null,
    });

    res.json({
      success: true,
      message: 'Account registered successfully',
      user: {
        id: newUser._id,
        email: newUser.email,
        name: newUser.name,
        phone: newUser.phone || '',
        role: newUser.role,
        isPaid: newUser.isPaid || newUser.role === 'admin',
      },
    });
  } catch (err) {
    console.error('Registration error:', err);
    res.status(500).json({ error: 'Failed to register account' });
  }
});

app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;
    if (!email) {
      return res.status(400).json({ error: 'Email is required' });
    }
    const cleanEmail = email.toLowerCase().trim();
    const db = await connectToDatabase();
    if (!db) {
      return res.status(503).json({ error: 'Database connection failed. Please ensure MongoDB Atlas Network Access has 0.0.0.0/0 whitelisted.' });
    }

    const user = await User.findOne({ email: cleanEmail });
    if (!user) {
      return res.status(401).json({ error: 'Account not found. Please register first.' });
    }

    // If password was provided, verify it
    if (user.passwordHash && user.salt) {
      if (!password) {
        return res.status(400).json({ error: 'Password is required' });
      }
      const isValid = verifyPassword(password, user.passwordHash, user.salt);
      if (!isValid) {
        return res.status(401).json({ error: 'Invalid password. Please try again.' });
      }
    } else if (password) {
      // Legacy user with no password hash yet: initialize their password
      const { hash, salt } = hashPassword(password);
      user.passwordHash = hash;
      user.salt = salt;
      await user.save();
    }

    const isAdmin = isUserAdmin(cleanEmail);

    if (isAdmin && (!user.isPaid || user.role !== 'admin')) {
      user.role = 'admin';
      user.isPaid = true;
      await user.save();
    }

    user.lastLoginAt = new Date();
    await user.save();

    res.json({
      success: true,
      user: {
        id: user._id,
        email: user.email,
        name: user.name,
        phone: user.phone || '',
        role: user.role,
        isPaid: user.isPaid || user.role === 'admin',
      },
    });
  } catch (err) {
    console.error('Login error:', err);
    res.status(500).json({ error: 'Failed to sign in' });
  }
});

// Change Password Endpoint
app.post('/api/auth/change-password', async (req, res) => {
  try {
    const { email, currentPassword, newPassword } = req.body;
    const authUser = await getAuthUser(req);
    const targetEmail = (authUser?.email || email || '').toLowerCase().trim();

    if (!targetEmail) {
      return res.status(401).json({ error: 'Unauthorized. Please sign in.' });
    }
    if (!currentPassword || !newPassword) {
      return res.status(400).json({ error: 'Both current password and new password are required' });
    }
    if (newPassword.length < 6) {
      return res.status(400).json({ error: 'New password must be at least 6 characters' });
    }

    await connectToDatabase();
    const user = await User.findOne({ email: targetEmail });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    // Verify current password
    if (user.passwordHash && user.salt) {
      const isValid = verifyPassword(currentPassword, user.passwordHash, user.salt);
      if (!isValid) {
        return res.status(401).json({ error: 'Current password is incorrect' });
      }
    }

    // Hash and update with new password
    const { hash, salt } = hashPassword(newPassword);
    user.passwordHash = hash;
    user.salt = salt;
    await user.save();

    res.json({ success: true, message: 'Password changed successfully!' });
  } catch (err) {
    console.error('Change password error:', err);
    res.status(500).json({ error: 'Failed to change password' });
  }
});

// Forgot Password - Step 1: Request Reset Code & Dispatch Verification Email
app.post('/api/auth/forgot-password', async (req, res) => {
  try {
    const { email } = req.body;
    if (!email) {
      return res.status(400).json({ error: 'Email is required' });
    }
    const cleanEmail = email.toLowerCase().trim();
    const db = await connectToDatabase();
    if (!db) {
      return res.status(503).json({ error: 'Database connection failed. Please ensure MongoDB Atlas Network Access has 0.0.0.0/0 whitelisted.' });
    }

    const user = await User.findOne({ email: cleanEmail });
    if (!user) {
      return res.status(404).json({ error: 'No account found with this email address' });
    }

    // Check if email service is configured
    if (!isEmailConfigured()) {
      console.warn(`⚠️ [Forgot Password] SMTP is not configured in .env.local! Cannot dispatch email to ${cleanEmail}.`);
      return res.status(503).json({
        error: 'Email delivery service is not configured. Please add SMTP credentials (SMTP_USER and SMTP_PASS) in .env.local to dispatch recovery emails.',
        needsSmtpConfig: true,
      });
    }

    // Generate 6-digit verification code valid for 15 minutes
    const resetCode = Math.floor(100000 + Math.random() * 900000).toString();
    user.resetCode = resetCode;
    user.resetCodeExpires = new Date(Date.now() + 15 * 60 * 1000); // 15 mins
    await user.save();

    // Dispatch real email via nodemailer transporter
    await sendPasswordResetEmail({
      to: user.email,
      name: user.name || 'Candidate',
      resetCode,
    });

    res.json({
      success: true,
      message: `A 6-digit verification code has been sent to ${user.email}. Please check your inbox.`,
    });
  } catch (err) {
    console.error('Forgot password error:', err);
    res.status(500).json({ error: err.message || 'Failed to send password recovery email' });
  }
});

// Forgot Password - Step 2: Verify Code and Reset Password
app.post('/api/auth/reset-password', async (req, res) => {
  try {
    const { email, resetCode, newPassword } = req.body;
    if (!email || !resetCode || !newPassword) {
      return res.status(400).json({ error: 'Email, reset code, and new password are required' });
    }
    if (newPassword.length < 6) {
      return res.status(400).json({ error: 'New password must be at least 6 characters' });
    }

    const cleanEmail = email.toLowerCase().trim();
    const db = await connectToDatabase();
    if (!db) {
      return res.status(503).json({ error: 'Database connection failed. Please ensure MongoDB Atlas Network Access has 0.0.0.0/0 whitelisted.' });
    }

    const user = await User.findOne({ email: cleanEmail });
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    if (!user.resetCode || user.resetCode !== resetCode.trim()) {
      return res.status(400).json({ error: 'Invalid reset code. Please check and try again.' });
    }

    if (new Date() > new Date(user.resetCodeExpires)) {
      return res.status(400).json({ error: 'Reset code has expired. Please request a new one.' });
    }

    // Update password
    const { hash, salt } = hashPassword(newPassword);
    user.passwordHash = hash;
    user.salt = salt;
    user.resetCode = null;
    user.resetCodeExpires = null;
    await user.save();

    res.json({ success: true, message: 'Password has been successfully reset! You can now log in.' });
  } catch (err) {
    console.error('Reset password error:', err);
    res.status(500).json({ error: 'Failed to reset password' });
  }
});

app.get('/api/auth/me', async (req, res) => {
  try {
    const user = await getAuthUser(req);
    if (!user) {
      return res.json({ user: null });
    }
    const isSuperAdmin = isUserAdmin(user.email);
    res.json({
      user: {
        id: user._id || user.id,
        email: user.email,
        name: user.name,
        phone: user.phone || '',
        role: isSuperAdmin ? 'admin' : 'user',
        isPaid: user.isPaid || isSuperAdmin,
      },
    });
  } catch (err) {
    console.error('/api/auth/me error:', err);
    res.status(500).json({ error: 'Failed to retrieve profile' });
  }
});

app.post('/api/auth/logout', (req, res) => {
  res.json({ success: true });
});

// ----------------------------------------------------
// 3. TESTS CATALOG ROUTE
// ----------------------------------------------------
const TEST_CATALOG = [
  {
    testId: 'demo-test-50',
    title: 'TSPLRB SI Free Demo Mock Test (50 Questions)',
    title_te: 'తెలంగాణ ఎస్సై ఉచిత డెమో మాక్ టెస్ట్ (50 ప్రశ్నలు)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Easy',
    totalQuestions: 50,
    totalMarks: 50,
    durationMinutes: 45,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: true,
    isUnlocked: true,
    description: 'Comprehensive 50-Question Free Demo featuring Arithmetic, Reasoning, and Current Affairs.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-3',
    title: 'TSPLRB SI Mock Test 3 (Easy • Foundational PWT)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 3 (సులభం • ప్రాథమిక స్థాయి PWT)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Easy',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Foundational 200Q paper focusing on core formulas, direct arithmetic, standard reasoning, and essential General Studies.',
  },
  {
    testId: 'tsplrb-si-mock-full-200',
    title: 'TSPLRB SI Full-Length Mock Test 1 (200 Questions)',
    title_te: 'తెలంగాణ ఎస్సై పూర్తి స్థాయి మాక్ టెస్ట్ 1 (200 ప్రశ్నలు)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Medium',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Official 200-Question Exam Pattern: 50 Arithmetic + 50 Reasoning + 100 General Studies & Telangana Movement.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-2',
    title: 'TSPLRB SI Full-Length Mock Test 2 (200 Questions)',
    title_te: 'తెలంగాణ ఎస్సై పూర్తి స్థాయి మాక్ టెస్ట్ 2 (200 ప్రశ్నలు)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Medium',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Advanced Practice Paper with In-depth Focus on Telangana History and High-Difficulty Reasoning.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-4',
    title: 'TSPLRB SI Mock Test 4 (Medium • Official Standard PWT)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 4 (మధ్యస్థం • అధికారిక ప్రామాణిక PWT)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Medium',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Exact calibration of the official TSPLRB SI 2022 Preliminary Exam. Standard multi-step word problems and official Telangana Movement history.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-5',
    title: 'TSPLRB SI Mock Test 5 (Hard • Advanced High-Yield PWT)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 5 (కఠినం • ఉన్నత స్థాయి స్పెషల్ PWT)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Hard',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'High-difficulty 200Q simulation modeling recent TSPSC and TSPLRB trends. Advanced statement-based questions, intricate puzzles, and in-depth governance.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-6',
    title: 'TSPLRB SI Mock Test 6 (Speed & Accuracy Practice PWT)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 6 (వేగం & కచ్చితత్వం సాధన PWT)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Medium',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'High-yield 200Q speed-building mock. Calibrated for optimal time allocation across Arithmetic, Reasoning, and General Studies with 2026 Current Affairs.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-7',
    title: 'TSPLRB SI Mock Test 7 (Hard • Grand Master Championship Simulation)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 7 (కఠినం • గ్రాండ్ మాస్టర్ ఛాంపియన్‌షిప్ సిమ్యులేషన్)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Hard',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Championship-tier 200Q simulation featuring multi-statement analytical GS, higher-order reasoning puzzles, and advanced arithmetic.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-8',
    title: 'TSPLRB SI Mock Test 8 (Medium • Official Standard PWT)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 8 (మధ్యస్థం • అధికారిక ప్రామాణిక PWT)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Medium',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Official 200Q Standard Blueprint: 50 Arithmetic + 50 Reasoning + 100 General Studies & Telangana Movement.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-9',
    title: 'TSPLRB SI Mock Test 9 (Advanced Practice & 2026 High-Yield PWT)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 9 (అడ్వాన్స్డ్ ప్రాక్టీస్ & 2026 స్పెషల్ PWT)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Hard',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Advanced Practice Paper integrating latest 2026 faculty questions, Telangana policies (HYDRAA, Bhoo Bharati, Caste Survey, Musi Project), and comprehensive Arithmetic & Reasoning.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-10',
    title: 'TSPLRB SI Mock Test 10 (Master Model Paper • Latest Civils & PWT Standard)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 10 (మాస్టర్ మోడల్ పేపర్ • సివిల్స్ & PWT ప్రమాణాలు)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Medium',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Master 200Q model paper calibrated on Civils/TSPSC standards: Speed-Distance-Time, Mensuration 2D/3D, PYQ Calendar Repetition, balanced GS weightage, international summits (BRICS/SCO/G20), and 2026 governance reforms.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-11',
    title: 'TSPLRB SI Mock Test 11 (High-Yield 2026 Reserve Bank • Final PWT Benchmark)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 11 (హై-యీల్డ్ 2026 రిజర్వ్ బ్యాంక్ • ఫైనల్ PWT బెంచ్‌మార్క్)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Hard',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'Comprehensive 200Q benchmark paper assembled from verified reserve faculty pools: Speed-Distance-Time, Mensuration 2D/3D, Calendar Repetition, Telangana Armed Struggle & Statehood, Indian Polity, National Movement, and 2026 Current Affairs.',
  },
  {
    testId: 'tsplrb-si-mock-full-200-12',
    title: 'TSPLRB SI Mock Test 12 (Easy • Foundational Speed & High-Accuracy PWT)',
    title_te: 'తెలంగాణ ఎస్సై మాక్ టెస్ట్ 12 (ఈజీ • ఫౌండేషనల్ స్పీడ్ & హై-ఆక్యురసీ PWT)',
    exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
    difficulty: 'Easy',
    totalQuestions: 200,
    totalMarks: 200,
    durationMinutes: 180,
    marksPerQuestion: 1.0,
    negativeMarking: 0.20,
    isFreeDemo: false,
    description: 'High-yield foundational 200Q paper designed for rapid solving, formula mastery, and concept reinforcement: Direct Arithmetic, Essential Reasoning, Core Polity Articles, Telangana Heritage & Statehood, and Vital Science.',
  },
];

app.get('/api/tests', async (req, res) => {
  try {
    const user = await getAuthUser(req);
    const isUnlocked = user?.isPaid || user?.role === 'admin';

    const tests = TEST_CATALOG.map(t => ({
      ...t,
      isUnlocked: t.isFreeDemo || isUnlocked,
    }));

    res.json({
      tests,
      userAccess: {
        isLoggedIn: !!user,
        email: user?.email || null,
        isPaid: isUnlocked,
        isAdmin: user?.role === 'admin',
      },
    });
  } catch (err) {
    console.error('/api/tests error:', err);
    res.status(500).json({ error: 'Failed to fetch test catalog' });
  }
});

function formatQuestionOptions(q) {
  if (Array.isArray(q.options) && q.options.length > 0) {
    return q.options.map((opt, i) => ({
      index: opt.index !== undefined ? opt.index : i,
      text_en: opt.text_en || (typeof opt === 'string' ? opt : ''),
      text_te: opt.text_te || opt.text_en || (typeof opt === 'string' ? opt : ''),
    }));
  }
  if (Array.isArray(q.options_en) && q.options_en.length > 0) {
    return q.options_en.map((opt_en, i) => ({
      index: i,
      text_en: opt_en,
      text_te: (q.options_te && q.options_te[i]) || opt_en,
    }));
  }
  return [];
}

// ----------------------------------------------------
// 4. QUESTIONS RETRIEVAL ROUTE
// ----------------------------------------------------
app.get('/api/tests/:id/questions', async (req, res) => {
  try {
    const { id } = req.params;
    const user = await getAuthUser(req);
    const isUnlocked = user?.isPaid || user?.role === 'admin';
    const isDemo = id === 'demo-test-50';

    if (!isDemo && !isUnlocked) {
      return res.status(402).json({
        error: 'Payment Required',
        message: 'This 200-question full exam requires full access. Unlock all exams for ₹99.',
        requiresPayment: true,
      });
    }

    let fileName = 'mock_test_full_200.json';
    if (id === 'tsplrb-si-mock-full-200-2') fileName = 'mock_test_full_200_2.json';
    else if (id === 'tsplrb-si-mock-full-200-3') fileName = 'mock_test_full_200_3.json';
    else if (id === 'tsplrb-si-mock-full-200-4') fileName = 'mock_test_full_200_4.json';
    else if (id === 'tsplrb-si-mock-full-200-5') fileName = 'mock_test_full_200_5.json';
    else if (id === 'tsplrb-si-mock-full-200-6') fileName = 'mock_test_full_200_6.json';
    else if (id === 'tsplrb-si-mock-full-200-7') fileName = 'mock_test_full_200_7.json';
    else if (id === 'tsplrb-si-mock-full-200-8') fileName = 'mock_test_full_200_8.json';
    else if (id === 'tsplrb-si-mock-full-200-9') fileName = 'mock_test_full_200_9.json';
    else if (id === 'tsplrb-si-mock-full-200-10') fileName = 'mock_test_full_200_10.json';
    else if (id === 'tsplrb-si-mock-full-200-11') fileName = 'mock_test_full_200_11.json';
    else if (id === 'tsplrb-si-mock-full-200-12') fileName = 'mock_test_full_200_12.json';

    const localFilePath = path.join(process.cwd(), 'public/data', fileName);
    let questionsData = [];

    if (fs.existsSync(localFilePath)) {
      const fileContent = fs.readFileSync(localFilePath, 'utf-8');
      const parsed = JSON.parse(fileContent);
      questionsData = parsed.questions || [];
    }

    if (isDemo && questionsData.length > 50) {
      const arith = questionsData.slice(0, 20);
      const reasoning = questionsData.slice(50, 65);
      const gs = questionsData.slice(100, 115);
      questionsData = [...arith, ...reasoning, ...gs].map((q, idx) => ({
        ...q,
        id: idx + 1,
        qNumber: idx + 1,
      }));
    }

    // Strip answers & explanations for exam integrity
    const sanitizedQuestions = questionsData.map(q => ({
      id: q.id || q.qNumber,
      qNumber: q.qNumber || q.id,
      section: q.section,
      topic: q.topic,
      question_en: q.question_en,
      question_te: q.question_te,
      options: formatQuestionOptions(q),
      marks: q.marks || 1.0,
      negativeMark: q.negativeMark || 0.20,
    }));

    res.json({
      testId: id,
      totalQuestions: sanitizedQuestions.length,
      durationMinutes: isDemo ? 45 : 180,
      marksPerQuestion: 1.0,
      negativeMarking: 0.20,
      questions: sanitizedQuestions,
    });
  } catch (err) {
    console.error('/api/tests/:id/questions error:', err);
    res.status(500).json({ error: 'Failed to load test questions' });
  }
});

// ----------------------------------------------------
// 5. TEST SUBMISSION & GRADING ROUTE
// ----------------------------------------------------
app.post('/api/tests/:id/submit', async (req, res) => {
  try {
    const { id } = req.params;
    const { answers = {}, startedAt, durationSeconds = 0, sectionTime = {} } = req.body;
    const user = await getAuthUser(req);
    const userEmail = user?.email || 'guest_demo@tsplrb.com';

    let fileName = 'mock_test_full_200.json';
    if (id === 'tsplrb-si-mock-full-200-2') fileName = 'mock_test_full_200_2.json';
    else if (id === 'tsplrb-si-mock-full-200-3') fileName = 'mock_test_full_200_3.json';
    else if (id === 'tsplrb-si-mock-full-200-4') fileName = 'mock_test_full_200_4.json';
    else if (id === 'tsplrb-si-mock-full-200-5') fileName = 'mock_test_full_200_5.json';
    else if (id === 'tsplrb-si-mock-full-200-6') fileName = 'mock_test_full_200_6.json';
    else if (id === 'tsplrb-si-mock-full-200-7') fileName = 'mock_test_full_200_7.json';
    else if (id === 'tsplrb-si-mock-full-200-8') fileName = 'mock_test_full_200_8.json';
    else if (id === 'tsplrb-si-mock-full-200-9') fileName = 'mock_test_full_200_9.json';
    else if (id === 'tsplrb-si-mock-full-200-10') fileName = 'mock_test_full_200_10.json';
    else if (id === 'tsplrb-si-mock-full-200-11') fileName = 'mock_test_full_200_11.json';
    else if (id === 'tsplrb-si-mock-full-200-12') fileName = 'mock_test_full_200_12.json';

    const localFilePath = path.join(process.cwd(), 'public/data', fileName);
    let masterQuestions = [];

    if (fs.existsSync(localFilePath)) {
      const fileContent = fs.readFileSync(localFilePath, 'utf-8');
      const parsed = JSON.parse(fileContent);
      masterQuestions = parsed.questions || [];
    }

    const isDemo = id === 'demo-test-50';
    if (isDemo && masterQuestions.length > 50) {
      const arith = masterQuestions.slice(0, 20);
      const reasoning = masterQuestions.slice(50, 65);
      const gs = masterQuestions.slice(100, 115);
      masterQuestions = [...arith, ...reasoning, ...gs].map((q, idx) => ({
        ...q,
        id: idx + 1,
        qNumber: idx + 1,
      }));
    }

    let correctCount = 0;
    let wrongCount = 0;
    let unansweredCount = 0;
    let totalScore = 0.0;

    const sectionBreakdown = {
      arithmetic: { name: 'Part A: Arithmetic', total: 0, correct: 0, wrong: 0, score: 0 },
      reasoning: { name: 'Part B: Reasoning', total: 0, correct: 0, wrong: 0, score: 0 },
      generalStudies: { name: 'Part C: General Studies', total: 0, correct: 0, wrong: 0, score: 0 },
    };

    const reviewQuestions = masterQuestions.map((q) => {
      const qNum = q.id || q.qNumber;
      const selected = answers[qNum] !== undefined && answers[qNum] !== null ? Number(answers[qNum]) : null;
      const correct = Number(
        q.correctOption !== undefined
          ? q.correctOption
          : q.correct_option !== undefined
          ? q.correct_option
          : 0
      );

      const sec = (q.section || '').toLowerCase();
      let secKey = 'generalStudies';
      if (sec.includes('arith') || qNum <= 50) secKey = 'arithmetic';
      else if (sec.includes('reason') || sec.includes('mental') || (qNum > 50 && qNum <= 100)) secKey = 'reasoning';

      if (sectionBreakdown[secKey]) {
        sectionBreakdown[secKey].total += 1;
      }

      let isCorrect = false;
      let isWrong = false;
      let marksEarned = 0;

      if (selected === null || selected === undefined) {
        unansweredCount += 1;
      } else if (selected === correct) {
        isCorrect = true;
        correctCount += 1;
        marksEarned = 1.0;
        totalScore += 1.0;
        if (sectionBreakdown[secKey]) {
          sectionBreakdown[secKey].correct += 1;
          sectionBreakdown[secKey].score += 1.0;
        }
      } else {
        isWrong = true;
        wrongCount += 1;
        marksEarned = -0.20;
        totalScore -= 0.20;
        if (sectionBreakdown[secKey]) {
          sectionBreakdown[secKey].wrong += 1;
          sectionBreakdown[secKey].score -= 0.20;
        }
      }

      return {
        id: qNum,
        qNumber: qNum,
        section: q.section,
        topic: q.topic,
        question_en: q.question_en,
        question_te: q.question_te,
        options: formatQuestionOptions(q),
        selectedOption: selected,
        correctOption: correct,
        isCorrect,
        isWrong,
        marksEarned,
        explanation_en: q.explanation_en,
        explanation_te: q.explanation_te,
      };
    });

    const totalQuestions = masterQuestions.length;
    const attemptedCount = correctCount + wrongCount;
    const accuracyPercent = attemptedCount > 0 ? Math.round((correctCount / attemptedCount) * 100) : 0;
    const finalScore = Number(totalScore.toFixed(2));

    // Save attempt to MongoDB
    let attemptId = `att_${Date.now()}`;
    const formattedSectionScores = [
      { 
        sectionKey: 'arithmetic',
        sectionName: sectionBreakdown.arithmetic.name, 
        score: Number(sectionBreakdown.arithmetic.score.toFixed(2)), 
        marksObtained: Number(sectionBreakdown.arithmetic.score.toFixed(2)), 
        correct: sectionBreakdown.arithmetic.correct, 
        correctCount: sectionBreakdown.arithmetic.correct, 
        wrong: sectionBreakdown.arithmetic.wrong, 
        wrongCount: sectionBreakdown.arithmetic.wrong, 
        total: sectionBreakdown.arithmetic.total, 
        maxMarks: sectionBreakdown.arithmetic.total, 
        timeSpentSeconds: Number(sectionTime.arithmetic || 0) 
      },
      { 
        sectionKey: 'reasoning',
        sectionName: sectionBreakdown.reasoning.name, 
        score: Number(sectionBreakdown.reasoning.score.toFixed(2)), 
        marksObtained: Number(sectionBreakdown.reasoning.score.toFixed(2)), 
        correct: sectionBreakdown.reasoning.correct, 
        correctCount: sectionBreakdown.reasoning.correct, 
        wrong: sectionBreakdown.reasoning.wrong, 
        wrongCount: sectionBreakdown.reasoning.wrong, 
        total: sectionBreakdown.reasoning.total, 
        maxMarks: sectionBreakdown.reasoning.total, 
        timeSpentSeconds: Number(sectionTime.reasoning || 0) 
      },
      { 
        sectionKey: 'general',
        sectionName: sectionBreakdown.generalStudies.name, 
        score: Number(sectionBreakdown.generalStudies.score.toFixed(2)), 
        marksObtained: Number(sectionBreakdown.generalStudies.score.toFixed(2)), 
        correct: sectionBreakdown.generalStudies.correct, 
        correctCount: sectionBreakdown.generalStudies.correct, 
        wrong: sectionBreakdown.generalStudies.wrong, 
        wrongCount: sectionBreakdown.generalStudies.wrong, 
        total: sectionBreakdown.generalStudies.total, 
        maxMarks: sectionBreakdown.generalStudies.total, 
        timeSpentSeconds: Number(sectionTime.generalStudies || sectionTime.general || 0) 
      },
    ];

    try {
      await connectToDatabase();
      if (user?._id) {
        const prevCount = await Attempt.countDocuments({ userId: user._id, testId: id });
        const newAttempt = await Attempt.create({
          userId: user._id,
          userEmail: user.email,
          testId: id,
          attemptNumber: prevCount + 1,
          startedAt: startedAt ? new Date(startedAt) : new Date(Date.now() - durationSeconds * 1000),
          submittedAt: new Date(),
          durationSeconds,
          totalScore: finalScore,
          totalMarks: totalQuestions,
          correctCount,
          wrongCount,
          unansweredCount,
          accuracyPercent,
          sectionScores: formattedSectionScores,
        });
        attemptId = newAttempt._id.toString();
      }
    } catch (saveErr) {
      console.warn('Could not persist attempt to MongoDB:', saveErr.message);
    }

    res.json({
      attemptId,
      testId: id,
      totalQuestions,
      totalMarks: totalQuestions,
      totalScore: finalScore,
      correctCount,
      wrongCount,
      unansweredCount,
      accuracyPercent,
      durationSeconds,
      sectionBreakdown: {
        arithmetic: {
          ...sectionBreakdown.arithmetic,
          timeSpentSeconds: Number(sectionTime.arithmetic || 0),
        },
        reasoning: {
          ...sectionBreakdown.reasoning,
          timeSpentSeconds: Number(sectionTime.reasoning || 0),
        },
        generalStudies: {
          ...sectionBreakdown.generalStudies,
          timeSpentSeconds: Number(sectionTime.generalStudies || sectionTime.general || 0),
        },
      },
      reviewQuestions,
    });
  } catch (err) {
    console.error('/api/tests/:id/submit error:', err);
    res.status(500).json({ error: 'Failed to process submission' });
  }
});

// ----------------------------------------------------
// 6. ATTEMPTS HISTORY ROUTE
// ----------------------------------------------------
app.get('/api/attempts', async (req, res) => {
  try {
    const user = await getAuthUser(req);
    if (!user) {
      return res.json({ attempts: [], stats: null });
    }

    await connectToDatabase();
    const attempts = await Attempt.find({ userEmail: user.email }).sort({ submittedAt: -1 }).lean();

    if (!attempts || attempts.length === 0) {
      return res.json({ attempts: [], stats: null });
    }

    let totalScoreSum = 0;
    let bestScore = -Infinity;
    let totalAccuracySum = 0;

    const formattedAttempts = attempts.map(att => {
      totalScoreSum += att.totalScore || 0;
      if ((att.totalScore || 0) > bestScore) bestScore = att.totalScore || 0;
      totalAccuracySum += att.accuracyPercent || 0;

      // Normalize sectionScores whether stored as Array, Object, or legacy
      let normalizedSections = [];
      const isDemo = att.testId?.includes('demo') || (att.totalMarks || 200) === 50;
      if (Array.isArray(att.sectionScores) && att.sectionScores.length > 0) {
        normalizedSections = att.sectionScores.map(s => {
          const secKey = s.sectionKey || (s.sectionName?.toLowerCase().includes('arith') ? 'arithmetic' : s.sectionName?.toLowerCase().includes('reason') ? 'reasoning' : 'general');
          const defaultMax = secKey === 'general' ? (isDemo ? 20 : 100) : (isDemo ? 15 : 50);
          return {
            sectionKey: secKey,
            sectionName: s.sectionName || (secKey === 'arithmetic' ? 'Part A: Arithmetic' : secKey === 'reasoning' ? 'Part B: Reasoning' : 'Part C: General Studies & Telangana'),
            score: Number(s.score ?? s.marksObtained ?? 0),
            correct: Number(s.correct ?? s.correctCount ?? 0),
            wrong: Number(s.wrong ?? s.wrongCount ?? 0),
            total: Number(s.total && s.total > 0 && !(s.total === 50 && defaultMax === 100) ? s.total : defaultMax),
            timeSpentSeconds: Number(s.timeSpentSeconds || 0),
          };
        });
      } else if (att.sectionScores && typeof att.sectionScores === 'object') {
        const raw = att.sectionScores;
        const isDemo = att.testId?.includes('demo') || (att.totalMarks || 200) === 50;
        const arithVal = raw.arithmetic ?? raw.arith ?? 0;
        const reasonVal = raw.reasoning ?? raw.reason ?? 0;
        const genVal = raw.generalStudies ?? raw.general ?? raw.gs ?? 0;

        const getScore = (val) => (typeof val === 'object' && val !== null ? Number(val.score ?? val.marksObtained ?? 0) : Number(val || 0));
        const getCorrect = (val) => (typeof val === 'object' && val !== null ? Number(val.correct ?? val.correctCount ?? 0) : 0);
        const getWrong = (val) => (typeof val === 'object' && val !== null ? Number(val.wrong ?? val.wrongCount ?? 0) : 0);
        const getTime = (val) => (typeof val === 'object' && val !== null ? Number(val.timeSpentSeconds ?? val.time ?? 0) : 0);

        normalizedSections = [
          {
            sectionKey: 'arithmetic',
            sectionName: 'Part A: Arithmetic',
            score: getScore(arithVal),
            correct: typeof arithVal === 'object' && arithVal !== null ? getCorrect(arithVal) : (att.correctCount || 0),
            wrong: typeof arithVal === 'object' && arithVal !== null ? getWrong(arithVal) : (att.wrongCount || 0),
            total: isDemo ? 15 : 50,
            timeSpentSeconds: getTime(arithVal),
          },
          {
            sectionKey: 'reasoning',
            sectionName: 'Part B: Reasoning',
            score: getScore(reasonVal),
            correct: getCorrect(reasonVal),
            wrong: getWrong(reasonVal),
            total: isDemo ? 15 : 50,
            timeSpentSeconds: getTime(reasonVal),
          },
          {
            sectionKey: 'general',
            sectionName: 'Part C: General Studies & Telangana',
            score: getScore(genVal),
            correct: getCorrect(genVal),
            wrong: getWrong(genVal),
            total: isDemo ? 20 : 100,
            timeSpentSeconds: getTime(genVal),
          },
        ];
      }

      // If timeSpentSeconds across all sections is 0, attribute duration to actual active section(s)
      const totalSecTime = normalizedSections.reduce((acc, s) => acc + (s.timeSpentSeconds || 0), 0);
      const testDuration = Number(att.durationSeconds || 0);
      if (totalSecTime === 0 && testDuration > 0 && normalizedSections.length > 0) {
        const arith = normalizedSections.find(s => s.sectionKey === 'arithmetic');
        const reason = normalizedSections.find(s => s.sectionKey === 'reasoning');
        const gen = normalizedSections.find(s => s.sectionKey === 'general');

        const arithAtt = (arith?.correct || 0) + (arith?.wrong || 0);
        const reasonAtt = (reason?.correct || 0) + (reason?.wrong || 0);
        const genAtt = (gen?.correct || 0) + (gen?.wrong || 0);

        if (arithAtt > 0 && reasonAtt === 0 && genAtt === 0) {
          if (arith) arith.timeSpentSeconds = testDuration;
        } else if (reasonAtt > 0 && arithAtt === 0 && genAtt === 0) {
          if (reason) reason.timeSpentSeconds = testDuration;
        } else if (genAtt > 0 && arithAtt === 0 && reasonAtt === 0) {
          if (gen) gen.timeSpentSeconds = testDuration;
        } else if (arithAtt + reasonAtt + genAtt > 0) {
          const totalAtt = arithAtt + reasonAtt + genAtt;
          const aT = Math.round(testDuration * (arithAtt / totalAtt));
          const rT = Math.round(testDuration * (reasonAtt / totalAtt));
          const gT = Math.max(0, testDuration - aT - rT);
          if (arith) arith.timeSpentSeconds = aT;
          if (reason) reason.timeSpentSeconds = rT;
          if (gen) gen.timeSpentSeconds = gT;
        } else {
          // If 0 questions answered, attribute duration to arithmetic (first section)
          if (arith) arith.timeSpentSeconds = testDuration;
        }
      }

      return {
        id: att._id.toString(),
        testId: att.testId,
        attemptNumber: att.attemptNumber || 1,
        totalScore: att.totalScore,
        totalMarks: att.totalMarks || 200,
        correctCount: att.correctCount,
        wrongCount: att.wrongCount,
        unansweredCount: att.unansweredCount,
        accuracyPercent: att.accuracyPercent,
        durationSeconds: att.durationSeconds,
        submittedAt: att.submittedAt,
        sectionScores: normalizedSections,
      };
    });

    const stats = {
      totalAttempts: formattedAttempts.length,
      bestScore: bestScore === -Infinity ? 0 : bestScore,
      averageScore: Number((totalScoreSum / formattedAttempts.length).toFixed(1)),
      averageAccuracy: Math.round(totalAccuracySum / formattedAttempts.length),
    };

    res.json({ attempts: formattedAttempts, stats });
  } catch (err) {
    console.error('/api/attempts error:', err);
    res.status(500).json({ error: 'Failed to load past attempts' });
  }
});

// ----------------------------------------------------
// 7. RAZORPAY PAYMENT ROUTES (LIVE PRODUCTION)
// ----------------------------------------------------
app.post('/api/payment/razorpay/create-order', async (req, res) => {
  try {
    const user = await getAuthUser(req);
    const userEmail = (req.body?.email || user?.email || '').toLowerCase().trim();
    const rawPhone = (req.body?.phone || user?.phone || '').toString().trim();
    // Normalize to 10-digit Indian phone number
    const cleanPhone = rawPhone.replace(/\D/g, '').replace(/^(91|0)/, '');

    if (!userEmail || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userEmail)) {
      return res.status(400).json({ error: 'Please enter a valid candidate email address' });
    }

    if (!cleanPhone || cleanPhone.length !== 10 || !/^[6-9]\d{9}$/.test(cleanPhone)) {
      return res.status(400).json({ error: 'Please enter a valid 10-digit Indian mobile number' });
    }

    // Save/update phone on user in DB
    try {
      await connectToDatabase();
      if (user?._id) {
        user.phone = cleanPhone;
        await user.save();
      } else if (userEmail) {
        await User.findOneAndUpdate({ email: userEmail }, { phone: cleanPhone });
      }
    } catch (phoneErr) {
      console.warn('Notice: could not update phone on user record:', phoneErr.message);
    }

    const keyId = process.env.RAZORPAY_KEY_ID;
    const keySecret = process.env.RAZORPAY_KEY_SECRET;

    const amount = Number(process.env.TEST_SERIES_PRICE || 99);
    const amountInPaise = amount * 100;

    const authHeader = 'Basic ' + Buffer.from(`${keyId}:${keySecret}`).toString('base64');
    const orderPayload = {
      amount: amountInPaise,
      currency: 'INR',
      receipt: `rcpt_${Date.now()}_${Math.random().toString(36).substring(7)}`,
      notes: {
        userEmail,
        userPhone: cleanPhone,
        examName: 'TSPLRB SI Mock Test Series',
      },
    };

    const rzpRes = await fetch('https://api.razorpay.com/v1/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: authHeader,
      },
      body: JSON.stringify(orderPayload),
    });

    const orderData = await rzpRes.json();
    if (!rzpRes.ok) {
      console.error('Razorpay Order API Error:', orderData);
      return res.status(500).json({ error: orderData.error?.description || 'Failed to create order' });
    }

    // Persist pending order to MongoDB
    try {
      await connectToDatabase();
      if (user?._id) {
        await Payment.create({
          userId: user._id,
          userEmail,
          userPhone: cleanPhone,
          amount,
          currency: 'INR',
          gateway: 'razorpay',
          transactionId: orderData.id,
          orderId: orderData.id,
          status: 'pending',
        });
      }
    } catch (dbErr) {
      console.warn('Payment record save notice:', dbErr.message);
    }

    res.json({
      success: true,
      orderId: orderData.id,
      amount: orderData.amount,
      currency: orderData.currency,
      keyId,
      email: userEmail,
      phone: cleanPhone,
    });
  } catch (err) {
    console.error('Create order error:', err);
    res.status(500).json({ error: 'Failed to create payment order' });
  }
});

app.post('/api/payment/razorpay/verify', async (req, res) => {
  try {
    const { razorpay_order_id, razorpay_payment_id, razorpay_signature, userEmail: bodyEmail } = req.body;
    if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature) {
      return res.status(400).json({ error: 'Missing payment signature details' });
    }

    const keySecret = process.env.RAZORPAY_KEY_SECRET;
    const expectedSignature = crypto
      .createHmac('sha256', keySecret)
      .update(`${razorpay_order_id}|${razorpay_payment_id}`)
      .digest('hex');

    if (expectedSignature !== razorpay_signature) {
      console.error('❌ Razorpay Signature Mismatch! Rejecting fraudulent request.');
      return res.status(400).json({ error: 'Invalid payment signature' });
    }

    const user = await getAuthUser(req);
    const userEmail = (user?.email || bodyEmail || '').toLowerCase();
    const cleanPhone = (req.body?.phone || user?.phone || '').toString().trim().replace(/\D/g, '').replace(/^(91|0)/, '');

    await connectToDatabase();
    if (userEmail) {
      let dbUser = await User.findOne({ email: userEmail });
      if (!dbUser) {
        dbUser = await User.create({
          email: userEmail,
          name: userEmail.split('@')[0],
          phone: cleanPhone || '',
          role: 'user',
          isPaid: true,
          accessGrantedBy: 'payment',
          accessGrantedAt: new Date(),
          notes: `Razorpay Payment ID: ${razorpay_payment_id}`,
        });
      } else {
        dbUser.isPaid = true;
        if (cleanPhone) {
          dbUser.phone = cleanPhone;
        }
        dbUser.accessGrantedBy = 'payment';
        dbUser.accessGrantedAt = new Date();
        dbUser.notes = `Razorpay Payment ID: ${razorpay_payment_id}`;
        await dbUser.save();
      }

      await Payment.findOneAndUpdate(
        { orderId: razorpay_order_id },
        {
          transactionId: razorpay_payment_id,
          status: 'completed',
          updatedAt: new Date(),
        },
        { upsert: false }
      );
    }

    res.json({
      success: true,
      message: 'Full access granted! All 200-question papers unlocked.',
      paymentId: razorpay_payment_id,
    });
  } catch (err) {
    console.error('Verify payment error:', err);
    res.status(500).json({ error: 'Payment verification failed' });
  }
});

// ----------------------------------------------------
// 8. ADMIN USER MANAGEMENT ROUTE
// ----------------------------------------------------
app.get('/api/admin/users', async (req, res) => {
  try {
    const user = await getAuthUser(req);
    if (!user || !isUserAdmin(user?.email)) {
      return res.status(403).json({ error: 'Unauthorized. Admin permissions required.' });
    }

    await connectToDatabase();
    // Ensure only varshithpoudala@gmail.com is ever stored as admin in DB
    await User.updateMany(
      { email: { $ne: 'varshithpoudala@gmail.com' }, role: 'admin' },
      { $set: { role: 'user' } }
    );
    const users = await User.find({}).sort({ createdAt: -1 }).lean();
    res.json({ users });
  } catch (err) {
    console.error('/api/admin/users error:', err);
    res.status(500).json({ error: 'Failed to fetch users' });
  }
});

app.post('/api/admin/users', async (req, res) => {
  try {
    const admin = await getAuthUser(req);
    if (!admin || !isUserAdmin(admin?.email)) {
      return res.status(403).json({ error: 'Unauthorized. Admin permissions required.' });
    }

    const { email, isPaid, role } = req.body;
    if (!email) return res.status(400).json({ error: 'Email is required' });

    await connectToDatabase();
    const updated = await User.findOneAndUpdate(
      { email: email.toLowerCase() },
      {
        isPaid: Boolean(isPaid),
        role: role || 'user',
        accessGrantedBy: isPaid ? 'admin' : null,
        accessGrantedAt: isPaid ? new Date() : null,
      },
      { new: true, upsert: true }
    );

    res.json({ success: true, user: updated });
  } catch (err) {
    console.error('/api/admin/users post error:', err);
    res.status(500).json({ error: 'Failed to update user' });
  }
});

// ----------------------------------------------------
// 8B. ADMIN TEST MANAGEMENT ROUTES
// ----------------------------------------------------
app.get('/api/admin/tests', async (req, res) => {
  try {
    const user = await getAuthUser(req);
    if (!user || !isUserAdmin(user?.email)) {
      return res.status(403).json({ error: 'Unauthorized. Admin permissions required.' });
    }
    res.json({ tests: TEST_CATALOG });
  } catch (err) {
    console.error('/api/admin/tests error:', err);
    res.status(500).json({ error: 'Failed to fetch test catalog' });
  }
});

app.post('/api/admin/tests', async (req, res) => {
  try {
    const user = await getAuthUser(req);
    if (!user || !isUserAdmin(user?.email)) {
      return res.status(403).json({ error: 'Unauthorized. Admin permissions required.' });
    }

    const {
      testId,
      title,
      title_te,
      difficulty = 'Medium',
      totalQuestions = 200,
      totalMarks = 200,
      durationMinutes = 180,
      negativeMarking = 0.20,
      isFreeDemo = false,
      description = '',
    } = req.body;

    if (!title) {
      return res.status(400).json({ error: 'Test title is required' });
    }

    const cleanId = (testId || `tsplrb-si-mock-full-200-${TEST_CATALOG.length}`)
      .toLowerCase()
      .trim()
      .replace(/\s+/g, '-');

    const existingIndex = TEST_CATALOG.findIndex(t => t.testId === cleanId);
    const newTest = {
      testId: cleanId,
      title: title.trim(),
      title_te: (title_te || title).trim(),
      exam: 'TSPLRB Sub-Inspector Preliminary Written Test (PWT)',
      difficulty,
      totalQuestions: Number(totalQuestions) || 200,
      totalMarks: Number(totalMarks) || 200,
      durationMinutes: Number(durationMinutes) || 180,
      marksPerQuestion: 1.0,
      negativeMarking: Number(negativeMarking) || 0.20,
      isFreeDemo: Boolean(isFreeDemo),
      description: description.trim() || 'Official simulated mock test calibrated for TSPLRB SI PWT 2026.',
    };

    if (existingIndex >= 0) {
      TEST_CATALOG[existingIndex] = newTest;
    } else {
      TEST_CATALOG.push(newTest);
    }

    res.json({
      success: true,
      message: `Mock test "${newTest.title}" created successfully!`,
      test: newTest,
      totalTests: TEST_CATALOG.length,
    });
  } catch (err) {
    console.error('/api/admin/tests post error:', err);
    res.status(500).json({ error: 'Failed to create mock test' });
  }
});

// ----------------------------------------------------
// 9. PRODUCTION STATIC FILE SERVING (SINGLE-PORT DEPLOYMENT)
// ----------------------------------------------------
const distPath = path.join(process.cwd(), 'dist');
if (fs.existsSync(distPath)) {
  console.log(`📦 Serving compiled Vite frontend from ${distPath}`);
  app.use(express.static(distPath));
  app.use((req, res, next) => {
    if (req.path.startsWith('/api')) return next();
    res.sendFile(path.join(distPath, 'index.html'));
  });
}

app.listen(PORT, () => {
  console.log(`🚀 TSPLRB SI Express API Server running on http://localhost:${PORT}`);
});
