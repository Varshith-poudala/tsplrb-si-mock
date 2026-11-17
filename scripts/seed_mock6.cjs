/**
 * Seed Mock Test 6 into MongoDB Atlas:
 * - tsplrb-si-mock-full-200-6
 */

const fs = require('fs');
const path = require('path');
const mongoose = require('mongoose');

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

const MONGODB_URI = process.env.MONGODB_URI;

async function seed() {
  if (!MONGODB_URI) {
    console.log('No MONGODB_URI found. Skipping DB seeding.');
    return;
  }

  console.log('🔄 Connecting to MongoDB Atlas...');
  await mongoose.connect(MONGODB_URI);
  console.log('✅ Connected to MongoDB Atlas.');

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

  const TestSchema = new mongoose.Schema({
    testId: { type: String, unique: true },
    title: String,
    title_te: String,
    exam: String,
    paper: String,
    difficulty: String,
    totalQuestions: Number,
    totalMarks: Number,
    durationMinutes: Number,
    marksPerQuestion: Number,
    negativeMarking: Number,
    sections: Array,
    isFreeDemo: Boolean,
  });
  const Test = mongoose.models.Test || mongoose.model('Test', TestSchema);

  const fpath = path.join(__dirname, '..', 'public/data/mock_test_full_200_6.json');
  const data = JSON.parse(fs.readFileSync(fpath, 'utf-8'));

  console.log(`\n📦 Seeding ${data.testId} (${data.questions.length} questions)...`);

  await Test.findOneAndUpdate(
    { testId: data.testId },
    {
      testId: data.testId,
      title: data.title,
      title_te: data.title_te,
      exam: data.exam,
      paper: data.paper,
      difficulty: data.difficulty,
      totalQuestions: data.totalQuestions,
      totalMarks: data.totalMarks,
      durationMinutes: data.durationMinutes,
      marksPerQuestion: data.marksPerQuestion,
      negativeMarking: data.negativeMarking,
      sections: data.sections,
      isFreeDemo: false,
    },
    { upsert: true, new: true }
  );

  await Question.deleteMany({ testId: data.testId });

  const qDocs = data.questions.map(q => ({
    testId: data.testId,
    qNumber: q.qNumber || q.id,
    section: q.section,
    topic: q.topic,
    question_en: q.question_en,
    question_te: q.question_te,
    options_en: q.options_en,
    options_te: q.options_te,
    correct_option: q.correct_option,
    explanation_en: q.explanation_en,
    explanation_te: q.explanation_te,
  }));

  await Question.insertMany(qDocs);
  console.log(`✅ Successfully seeded ${qDocs.length} questions for ${data.testId} into MongoDB Atlas!`);

  await mongoose.disconnect();
}

seed().catch(err => {
  console.error('Seeding error:', err);
  process.exit(1);
});
