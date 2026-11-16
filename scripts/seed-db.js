/**
 * MongoDB Atlas Seeder Script for TSPLRB SI Mock Test Platform
 * Usage: node scripts/seed-db.js
 */

const fs = require('fs');
const path = require('path');
const mongoose = require('mongoose');

// Read environment from .env.local or process.env
const envPath = path.join(__dirname, '..', '.env.local');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf-8');
  envContent.split('\n').forEach(line => {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#') && trimmed.includes('=')) {
      const [key, ...vals] = trimmed.split('=');
      const val = vals.join('=').trim().replace(/^["']|["']$/g, '');
      if (!process.env[key.trim()]) {
        process.env[key.trim()] = val;
      }
    }
  });
}

const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://localhost:27017/tsplrb_cbt';
const ADMIN_EMAILS = (process.env.ADMIN_EMAILS || 'varshithpoudala@gmail.com').toLowerCase().split(',').map(e => e.trim());

async function runSeed() {
  console.log('🔄 Connecting to MongoDB at:', MONGODB_URI.replace(/:([^:@]{4})[^:@]*@/, ':****@'));
  
  try {
    await mongoose.connect(MONGODB_URI);
    console.log('✅ Connected to MongoDB successfully.');

    // 1. Define or use schemas
    const UserSchema = new mongoose.Schema({
      email: { type: String, unique: true, lowercase: true, trim: true },
      name: String,
      role: { type: String, default: 'user' },
      isPaid: { type: Boolean, default: false },
      accessGrantedBy: String,
      accessGrantedAt: Date,
      notes: String,
      createdAt: { type: Date, default: Date.now },
    });
    const User = mongoose.models.User || mongoose.model('User', UserSchema);

    const QuestionSchema = new mongoose.Schema({
      testId: { type: String, index: true },
      qNumber: Number,
      section: String,
      topic: String,
      question_en: String,
      question_te: String,
      options_en: [String],
      options_te: [String],
      correct_option: Number,
      explanation_en: String,
      explanation_te: String,
    });
    const Question = mongoose.models.Question || mongoose.model('Question', QuestionSchema);

    // 2. Ensure Super Admin user exists with full permissions
    for (const adminEmail of ADMIN_EMAILS) {
      const existingAdmin = await User.findOne({ email: adminEmail });
      if (!existingAdmin) {
        await User.create({
          email: adminEmail,
          name: 'Varshith (Super Admin)',
          role: 'admin',
          isPaid: true,
          accessGrantedBy: 'admin',
          accessGrantedAt: new Date(),
          notes: 'Master Administrator Account',
        });
        console.log(`👑 Created Super Admin account: ${adminEmail}`);
      } else {
        existingAdmin.role = 'admin';
        existingAdmin.isPaid = true;
        existingAdmin.accessGrantedBy = 'admin';
        await existingAdmin.save();
        console.log(`👑 Verified & Updated Super Admin account: ${adminEmail}`);
      }
    }

    // 3. Load verified 200 questions from JSON
    const jsonPath = path.join(__dirname, '..', 'public', 'data', 'mock_test_full_200.json');
    if (!fs.existsSync(jsonPath)) {
      console.error('❌ Could not find mock_test_full_200.json at', jsonPath);
      process.exit(1);
    }

    const rawData = fs.readFileSync(jsonPath, 'utf-8');
    const parsed = JSON.parse(rawData);
    const questions = parsed.questions || [];

    console.log(`📖 Found ${questions.length} questions in JSON.`);

    // 4. Seed into Question collection for 'tsplrb-si-mock-full-200'
    console.log('🌱 Upserting 200 questions into MongoDB Question collection...');
    let insertedCount = 0;

    for (const q of questions) {
      const qNum = q.id || q.qNumber;
      await Question.findOneAndUpdate(
        { testId: 'tsplrb-si-mock-full-200', qNumber: qNum },
        {
          testId: 'tsplrb-si-mock-full-200',
          qNumber: qNum,
          section: q.section,
          topic: q.topic || '',
          question_en: q.question_en,
          question_te: q.question_te,
          options_en: q.options_en,
          options_te: q.options_te,
          correct_option: q.correct_option,
          explanation_en: q.explanation_en,
          explanation_te: q.explanation_te,
        },
        { upsert: true, new: true }
      );
      insertedCount++;
    }

    console.log(`✅ Successfully seeded ${insertedCount} questions for Full Test 1!`);

    // 5. Seed 50 questions for 'demo-test-50' (Free Demo Test)
    console.log('🌱 Upserting 50 representative questions for Free Demo Test...');
    const demoQuestions = [
      ...questions.slice(0, 20),   // Arithmetic
      ...questions.slice(50, 65),  // Reasoning
      ...questions.slice(100, 115) // GS / Current Affairs
    ];

    for (let i = 0; i < demoQuestions.length; i++) {
      const q = demoQuestions[i];
      const qNum = i + 1;
      await Question.findOneAndUpdate(
        { testId: 'demo-test-50', qNumber: qNum },
        {
          testId: 'demo-test-50',
          qNumber: qNum,
          section: q.section,
          topic: q.topic || '',
          question_en: q.question_en,
          question_te: q.question_te,
          options_en: q.options_en,
          options_te: q.options_te,
          correct_option: q.correct_option,
          explanation_en: q.explanation_en,
          explanation_te: q.explanation_te,
        },
        { upsert: true, new: true }
      );
    }
    console.log(`✅ Successfully seeded 50 questions for Free Demo Test!`);

    console.log('\n🎉 Database Seeding Complete!');
    process.exit(0);
  } catch (err) {
    console.error('❌ Seeding error:', err);
    process.exit(1);
  }
}

runSeed();
