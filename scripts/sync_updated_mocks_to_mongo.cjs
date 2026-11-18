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

async function sync() {
  if (!MONGODB_URI) {
    console.log('No MONGODB_URI found.');
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

  const testsToSync = [
    { testId: 'tsplrb-si-mock-full-200-3', file: 'mock_test_full_200_3.json' },
    { testId: 'tsplrb-si-mock-full-200-4', file: 'mock_test_full_200_4.json' },
    { testId: 'tsplrb-si-mock-full-200-5', file: 'mock_test_full_200_5.json' },
    { testId: 'tsplrb-si-mock-full-200-6', file: 'mock_test_full_200_6.json' },
    { testId: 'tsplrb-si-mock-full-200-8', file: 'mock_test_full_200_8.json' },
    { testId: 'tsplrb-si-mock-full-200-9', file: 'mock_test_full_200_9.json' },
  ];

  for (const t of testsToSync) {
    const filePath = path.join(__dirname, '..', 'public', 'data', t.file);
    if (!fs.existsSync(filePath)) {
      console.log(`File not found: ${filePath}`);
      continue;
    }
    const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    const questions = data.questions || [];

    console.log(`\n⏳ Syncing ${t.testId} (${questions.length} questions)...`);
    await Question.deleteMany({ testId: t.testId });

    const docs = questions.map((q, idx) => ({
      testId: t.testId,
      qNumber: q.qNumber || q.id || idx + 1,
      section: q.section || 'General Studies',
      topic: q.topic || 'General',
      question_en: q.question_en,
      question_te: q.question_te,
      options_en: q.options_en || (q.options ? q.options.map(o => o.text_en) : []),
      options_te: q.options_te || (q.options ? q.options.map(o => o.text_te) : []),
      correct_option: q.correct_option !== undefined ? q.correct_option : 0,
      explanation_en: q.explanation_en || '',
      explanation_te: q.explanation_te || '',
    }));

    await Question.insertMany(docs);
    console.log(`✅ Successfully synced ${docs.length} questions for ${t.testId}`);
  }

  console.log('\n🎉 ALL UPDATED MOCK TESTS SYNCED TO MONGODB ATLAS!');
  await mongoose.disconnect();
}

sync().catch(err => {
  console.error('Sync failed:', err);
  process.exit(1);
});
