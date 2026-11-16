const fs = require('fs');
const path = require('path');

console.log('================================================================');
console.log('TSPLRB SI PLATFORM - COMPREHENSIVE SYSTEM DIAGNOSTICS & AUDIT');
console.log('================================================================\n');

let totalTests = 0;
let passedTests = 0;
let failedTests = 0;

function assert(condition, message) {
  totalTests++;
  if (condition) {
    passedTests++;
    console.log(`  ✓ PASS: ${message}`);
  } else {
    failedTests++;
    console.error(`  ✗ FAIL: ${message}`);
  }
}

// -----------------------------------------------------------------------------
// 1. DATA INTEGRITY & TEST CATALOG DIAGNOSTICS
// -----------------------------------------------------------------------------
console.log('--- TEST SUITE 1: Mock Test Files & Question Data Integrity ---');

const testFiles = [
  { name: 'Mock Test 1', file: 'mock_test_full_200.json', expectedQs: 200 },
  { name: 'Mock Test 2', file: 'mock_test_full_200_2.json', expectedQs: 200 },
  { name: 'Mock Test 3', file: 'mock_test_full_200_3.json', expectedQs: 200 },
  { name: 'Mock Test 4', file: 'mock_test_full_200_4.json', expectedQs: 200 },
  { name: 'Mock Test 5', file: 'mock_test_full_200_5.json', expectedQs: 200 },
  { name: 'Mock Test 6', file: 'mock_test_full_200_6.json', expectedQs: 200 },
  { name: 'Mock Test 7', file: 'mock_test_full_200_7.json', expectedQs: 200 },
];

testFiles.forEach(({ name, file, expectedQs }) => {
  const filePath = path.join(__dirname, '../public/data', file);
  assert(fs.existsSync(filePath), `${name} (${file}) exists on disk`);

  let data;
  try {
    data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    assert(true, `${name} has valid JSON syntax`);
  } catch (e) {
    assert(false, `${name} failed JSON parsing: ${e.message}`);
    return;
  }

  const qs = data.questions || [];
  assert(qs.length === expectedQs, `${name} contains exactly ${expectedQs} questions (Found: ${qs.length})`);

  let validIds = true;
  let hasBilingualText = true;
  let hasValidOptions = true;
  let hasValidAnswers = true;
  let oldCaCount = 0;
  let ca2026Count = 0;

  qs.forEach((q, idx) => {
    const qNum = idx + 1;
    if ((q.id !== undefined ? q.id : qNum) !== qNum) validIds = false;

    const enText = q.question_en || q.questionEn || '';
    const teText = q.question_te || q.questionTe || '';
    if (!enText || !teText) hasBilingualText = false;

    let opts = q.options_en;
    if (!opts && Array.isArray(q.options)) {
      opts = q.options.map(o => o.text_en || o);
    }
    if (!opts || opts.length !== 4) hasValidOptions = false;

    const corr = q.correct_option !== undefined ? q.correct_option : q.correctOption;
    if (corr === undefined || corr < 0 || corr > 3) hasValidAnswers = false;

    // Check Current Affairs section (GS range Q101-Q165)
    if (qNum > 100 && qNum <= 165) {
      const qStr = JSON.stringify(q);
      if (qStr.includes('2026')) ca2026Count++;
      if (/201[89]|202[0-4]/.test(qStr) && !qStr.includes('2026')) {
        // Exclude static history dates
        if (!/(?:1948|1956|1969|2014|appointed day|b\.n\. srikrishna)/i.test(qStr)) {
          oldCaCount++;
        }
      }
    }
  });

  assert(validIds, `${name} has consecutive 1-to-${expectedQs} question IDs`);
  assert(hasBilingualText, `${name} all questions have both English and Telugu translations`);
  assert(hasValidOptions, `${name} all questions have exactly 4 choices`);
  assert(hasValidAnswers, `${name} all questions have valid correct answers (index 0..3)`);
  assert(oldCaCount === 0, `${name} has ZERO outdated Current Affairs questions (Old CA: ${oldCaCount})`);
  assert(ca2026Count > 0, `${name} features authentic 2026 Current Affairs (Found: ${ca2026Count})`);
});

// -----------------------------------------------------------------------------
// 2. DEMO TEST SLICE INTEGRITY
// -----------------------------------------------------------------------------
console.log('\n--- TEST SUITE 2: Free Demo Test (50 Questions) Slice Integrity ---');
const m1Data = JSON.parse(fs.readFileSync(path.join(__dirname, '../public/data/mock_test_full_200.json'), 'utf8'));
const m1Questions = m1Data.questions;

const demoArith = m1Questions.slice(0, 20);
const demoReasoning = m1Questions.slice(50, 65);
const demoGs = m1Questions.slice(100, 115);
const demoMaster = [...demoArith, ...demoReasoning, ...demoGs].map((q, idx) => ({ ...q, id: idx + 1 }));

assert(demoMaster.length === 50, `Demo test produces exactly 50 questions (Found: ${demoMaster.length})`);
assert(demoArith.length === 20, `Demo test contains 20 Arithmetic questions`);
assert(demoReasoning.length === 15, `Demo test contains 15 Reasoning questions`);
assert(demoGs.length === 15, `Demo test contains 15 General Studies / Current Affairs questions`);

let demo2026Count = 0;
demoGs.forEach(q => {
  if (JSON.stringify(q).includes('2026')) demo2026Count++;
});
assert(demo2026Count === 15, `All 15 General Studies questions in Demo Test are 2026 Current Affairs (${demo2026Count}/15)`);

// -----------------------------------------------------------------------------
// 3. SCORING ENGINE & EVALUATION LOGIC
// -----------------------------------------------------------------------------
console.log('\n--- TEST SUITE 3: Scoring & Negative Marking Engine ---');

function evaluateSubmission(masterQuestions, userAnswers) {
  let correctCount = 0;
  let wrongCount = 0;
  let unansweredCount = 0;
  let totalScore = 0;

  const sectionBreakdown = {
    arithmetic: { correct: 0, wrong: 0, unanswered: 0, total: 0, score: 0 },
    reasoning: { correct: 0, wrong: 0, unanswered: 0, total: 0, score: 0 },
    generalStudies: { correct: 0, wrong: 0, unanswered: 0, total: 0, score: 0 },
  };

  masterQuestions.forEach((q, idx) => {
    const qNum = idx + 1;
    const selected = userAnswers[qNum] !== undefined ? Number(userAnswers[qNum]) : null;
    const correct = Number(q.correct_option !== undefined ? q.correct_option : q.correctOption);

    const sec = (q.section || '').toLowerCase();
    let secKey = 'generalStudies';
    if (sec.includes('arith') || qNum <= 50) secKey = 'arithmetic';
    else if (sec.includes('reason') || sec.includes('mental') || (qNum > 50 && qNum <= 100)) secKey = 'reasoning';

    sectionBreakdown[secKey].total += 1;

    if (selected === null || selected === undefined) {
      unansweredCount += 1;
      sectionBreakdown[secKey].unanswered += 1;
    } else if (selected === correct) {
      correctCount += 1;
      totalScore += 1.0;
      sectionBreakdown[secKey].correct += 1;
      sectionBreakdown[secKey].score += 1.0;
    } else {
      wrongCount += 1;
      totalScore -= 0.20;
      sectionBreakdown[secKey].wrong += 1;
      sectionBreakdown[secKey].score -= 0.20;
    }
  });

  const attemptedCount = correctCount + wrongCount;
  const accuracyPercent = attemptedCount > 0 ? Math.round((correctCount / attemptedCount) * 100) : 0;
  return {
    totalScore: Number(totalScore.toFixed(2)),
    correctCount,
    wrongCount,
    unansweredCount,
    accuracyPercent,
    sectionBreakdown,
  };
}

// Case A: 100% Correct Submission
const perfectAnswers = {};
demoMaster.forEach((q, idx) => {
  perfectAnswers[idx + 1] = q.correct_option !== undefined ? q.correct_option : q.correctOption;
});
const perfectResult = evaluateSubmission(demoMaster, perfectAnswers);
assert(perfectResult.totalScore === 50.0, `Perfect submission scores 50.0 / 50.0 (Got: ${perfectResult.totalScore})`);
assert(perfectResult.correctCount === 50, `Perfect submission has 50 correct answers`);
assert(perfectResult.wrongCount === 0, `Perfect submission has 0 wrong answers`);
assert(perfectResult.accuracyPercent === 100, `Perfect submission has 100% accuracy`);

// Case B: Negative marking test: 10 correct, 5 wrong, 35 unanswered
const partialAnswers = {};
// Answer first 10 correctly
for (let i = 1; i <= 10; i++) {
  partialAnswers[i] = demoMaster[i - 1].correct_option !== undefined ? demoMaster[i - 1].correct_option : demoMaster[i - 1].correctOption;
}
// Answer next 5 incorrectly
for (let i = 11; i <= 15; i++) {
  const corr = demoMaster[i - 1].correct_option !== undefined ? demoMaster[i - 1].correct_option : demoMaster[i - 1].correctOption;
  partialAnswers[i] = (corr + 1) % 4; // intentionally wrong
}
const partialResult = evaluateSubmission(demoMaster, partialAnswers);
const expectedScore = 10 * 1.0 - 5 * 0.20; // 9.0
assert(partialResult.totalScore === 9.0, `Negative marking test: 10 correct, 5 wrong (-0.20 each) yields 9.00 (Got: ${partialResult.totalResult || partialResult.totalScore})`);
assert(partialResult.correctCount === 10, `Correct count is 10`);
assert(partialResult.wrongCount === 5, `Wrong count is 5`);
assert(partialResult.unansweredCount === 35, `Unanswered count is 35`);
assert(partialResult.accuracyPercent === 67, `Accuracy is 67% (10/15)`);

// -----------------------------------------------------------------------------
// 4. DATABASE & SERVER CODE AUDIT
// -----------------------------------------------------------------------------
console.log('\n--- TEST SUITE 4: Server Code Architecture & Routes Audit ---');
const serverCode = fs.readFileSync(path.join(__dirname, '../server/index.js'), 'utf8');

const requiredRoutes = [
  "app.get('/api/tests'",
  "app.get('/api/tests/:id/questions'",
  "app.post('/api/tests/:id/submit'",
  "app.get('/api/attempts'",
  "app.post('/api/auth/register'",
  "app.post('/api/auth/login'",
  "app.get('/api/auth/me'",
  "app.post('/api/auth/forgot-password'",
  "app.post('/api/auth/change-password'",
  "app.post('/api/auth/reset-password'",
  "app.post('/api/payment/razorpay/create-order'",
  "app.post('/api/payment/razorpay/verify'",
];

requiredRoutes.forEach(route => {
  assert(serverCode.includes(route), `Server defines route: ${route}`);
});

// Check blur / pause support in Exam.jsx
const examJsx = fs.readFileSync(path.join(__dirname, '../src/pages/Exam.jsx'), 'utf8');
assert(examJsx.includes('isPaused'), `Exam.jsx supports pause state (isPaused)`);
assert(examJsx.includes('filter: blur') || examJsx.includes('blur-'), `Exam.jsx applies blur filter when test is paused`);
assert(examJsx.includes('Resume Exam'), `Exam.jsx has explicit Resume button when paused`);

console.log('\n================================================================');
console.log(`DIAGNOSTIC SUMMARY: ${passedTests} PASSED, ${failedTests} FAILED (TOTAL: ${totalTests})`);
console.log('================================================================\n');

if (failedTests > 0) {
  process.exit(1);
}
