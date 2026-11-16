/**
 * Seed all mock tests into MongoDB Atlas:
 * - tsplrb-si-mock-full-200-3 (Easy)
 * - tsplrb-si-mock-full-200-4 (Medium)
 * - tsplrb-si-mock-full-200-5 (Tough)
 * - tsplrb-si-mock-full-200 (Mock 1)
 * - demo-test-50 (Demo 50)
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

  const files = [
    { file: 'mock_test_full_200.json', testId: 'tsplrb-si-mock-full-200' },
    { file: 'mock_test_full_200_2.json', testId: 'tsplrb-si-mock-full-200-2' },
    { file: 'mock_test_full_200_3.json', testId: 'tsplrb-si-mock-full-200-3' },
    { file: 'mock_test_full_200_4.json', testId: 'tsplrb-si-mock-full-200-4' },
    { file: 'mock_test_full_200_5.json', testId: 'tsplrb-si-mock-full-200-5' },
  ];

  for (const item of files) {
    const fpath = path.join(__dirname, '..', 'public/data', item.file);
    if (!fs.existsSync(fpath)) continue;
    const data = JSON.parse(fs.readFileSync(fpath, 'utf-8'));

    console.log(`\n📦 Seeding ${item.testId} (${data.questions.length} questions)...`);

    await Test.findOneAndUpdate(
      { testId: item.testId },
      {
        testId: item.testId,
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

    await Question.deleteMany({ testId: item.testId });

    const qDocs = data.questions.map(q => ({
      testId: item.testId,
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
    console.log(`✅ Seeded ${qDocs.length} questions for ${item.testId}.`);
  }

  console.log('\n🎉 ALL MOCK TESTS SEEDED TO MONGODB SUCCESSFULLY!');
  await mongoose.disconnect();
}

seed().catch(err => {
  console.error('Seeding error:', err);
  process.exit(1);
});
