/**
 * TSPLRB SI Prelims Daily Mock Test - Application Engine
 * Handles 100 Bilingual Questions, 3-Hour Timer, 10-per-page Pagination,
 * Section Navigation, Question Jump, Palette, and WhatsApp Sharing.
 */

(function () {
  'use strict';

  // Constants
  const TOTAL_QUESTIONS = 100;
  const QUESTIONS_PER_PAGE = 10;
  const TOTAL_PAGES = 10;
  const EXAM_DURATION_SECONDS = 3 * 60 * 60; // 3 Hours (10800s)
  const NEGATIVE_MARK = 0.20;
  const STORAGE_KEY = 'tsplrb_mock_test_1_state';

  // App State
  let state = {
    questions: [],
    candidateName: '',
    currentPage: 1,
    activeSectionFilter: 'all', // 'all', 'arithmetic', 'reasoning'
    paletteFilter: 'all',
    solutionFilter: 'all',
    userAnswers: {},       // { qId: optionIndex (0-3) }
    markedForReview: {},   // { qId: boolean }
    visitedQuestions: {},  // { qId: boolean }
    timeRemaining: EXAM_DURATION_SECONDS,
    isStarted: false,
    isSubmitted: false,
    startTime: null,
    endTime: null
  };

  let timerInterval = null;

  // DOM Elements
  const homeView = document.getElementById('homeView');
  const examView = document.getElementById('examView');
  const resultView = document.getElementById('resultView');
  
  const examHeaderTools = document.getElementById('examHeaderTools');
  const timerDisplay = document.getElementById('timerDisplay');
  const timerBox = document.getElementById('timerBox');
  const jumpInput = document.getElementById('jumpInput');
  const jumpBtn = document.getElementById('jumpBtn');
  
  const candidateNameInput = document.getElementById('candidateName');
  const startTestBtn = document.getElementById('startTestBtn');
  
  const questionsContainer = document.getElementById('questionsContainer');
  const currentPageIndicator = document.getElementById('currentPageIndicator');
  const currentQuestionRange = document.getElementById('currentQuestionRange');
  const prevPageBtn = document.getElementById('prevPageBtn');
  const nextPageBtn = document.getElementById('nextPageBtn');
  const paginationNumbers = document.getElementById('paginationNumbers');
  
  const questionGrid = document.getElementById('questionGrid');
  const countAnswered = document.getElementById('countAnswered');
  const countUnanswered = document.getElementById('countUnanswered');
  const countMarked = document.getElementById('countMarked');
  const countNotVisited = document.getElementById('countNotVisited');

  const headerSubmitBtn = document.getElementById('headerSubmitBtn');
  const sidebarSubmitBtn = document.getElementById('sidebarSubmitBtn');
  const submitModal = document.getElementById('submitModal');
  const cancelSubmitBtn = document.getElementById('cancelSubmitBtn');
  const confirmSubmitBtn = document.getElementById('confirmSubmitBtn');
  
  const modalAnswered = document.getElementById('modalAnswered');
  const modalUnanswered = document.getElementById('modalUnanswered');
  const modalMarked = document.getElementById('modalMarked');

  const testSelect = document.getElementById('testSelect');
  const shareWhatsappHeaderBtn = document.getElementById('shareWhatsappHeaderBtn');
  const whatsappShareResultBtn = document.getElementById('whatsappShareResultBtn');
  const retakeTestBtn = document.getElementById('retakeTestBtn');

  // Initialize
  async function init() {
    try {
      // Determine test file from URL or dropdown
      const urlParams = new URLSearchParams(window.location.search);
      let selectedTest = urlParams.get('test') || (testSelect ? testSelect.value : 'mock_test_1.json');
      if (testSelect) {
        testSelect.value = selectedTest;
        testSelect.addEventListener('change', (e) => {
          localStorage.removeItem(STORAGE_KEY);
          window.location.search = `?test=${e.target.value}`;
        });
      }

      const response = await fetch(`data/${selectedTest}`);
      if (!response.ok) throw new Error(`Failed to load ${selectedTest}`);
      const data = await response.json();
      
      // Normalize questions to guarantee { options: [{label, text_en, text_te}], correct_answer }
      state.questions = (data.questions || []).map((q, qIndex) => {
        let opts = [];
        if (Array.isArray(q.options) && q.options.length > 0 && typeof q.options[0] === 'object') {
          opts = q.options;
        } else if (Array.isArray(q.options_en)) {
          opts = q.options_en.map((en, idx) => ({
            label: ['A', 'B', 'C', 'D'][idx] || String(idx + 1),
            text_en: String(en),
            text_te: (q.options_te && q.options_te[idx]) ? String(q.options_te[idx]) : String(en)
          }));
        } else if (Array.isArray(q.options)) {
          opts = q.options.map((en, idx) => ({
            label: ['A', 'B', 'C', 'D'][idx] || String(idx + 1),
            text_en: String(en),
            text_te: String(en)
          }));
        }

        const correctAns = (q.correct_answer !== undefined) ? q.correct_answer : 
                           (q.correct_option !== undefined ? q.correct_option : 0);

        return {
          id: q.id || (qIndex + 1),
          section: q.section || (qIndex < 50 ? 'Arithmetic' : 'Reasoning & Mental Ability'),
          topic: q.topic || 'General',
          question_en: q.question_en || '',
          question_te: q.question_te || q.question_en || '',
          options: opts,
          correct_answer: correctAns,
          explanation_en: q.explanation_en || 'Refer to standard formula.',
          explanation_te: q.explanation_te || q.explanation_en || 'ప్రామాణిక సూత్రాన్ని చూడండి.'
        };
      });
      
      // Load saved state if available
      loadSavedState();

      setupEventListeners();
      renderPaginationControls();
      
      if (state.isSubmitted) {
        showResults();
      } else if (state.isStarted) {
        resumeExam();
      }
    } catch (err) {
      console.error(err);
      alert('Error loading exam questions. Please refresh or verify data file.');
    }
  }

  // Event Listeners Setup
  function setupEventListeners() {
    startTestBtn.addEventListener('click', startExam);

    prevPageBtn.addEventListener('click', () => {
      if (state.currentPage > 1) goToPage(state.currentPage - 1);
    });

    nextPageBtn.addEventListener('click', () => {
      if (state.currentPage < TOTAL_PAGES) goToPage(state.currentPage + 1);
    });

    // Jump to Question
    jumpBtn.addEventListener('click', handleJump);
    jumpInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') handleJump();
    });

    // Section tabs on top
    document.querySelectorAll('.section-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        document.querySelectorAll('.section-tab').forEach(t => t.classList.remove('active'));
        e.target.classList.add('active');
        const section = e.target.dataset.section;
        state.activeSectionFilter = section;
        if (section === 'arithmetic') {
          goToPage(1);
        } else if (section === 'reasoning') {
          goToPage(6);
        }
      });
    });

    // Palette Filter Tabs
    document.querySelectorAll('.pal-tab').forEach(tab => {
      tab.addEventListener('click', (e) => {
        document.querySelectorAll('.pal-tab').forEach(t => t.classList.remove('active'));
        e.target.classList.add('active');
        state.paletteFilter = e.target.dataset.filter;
        renderQuestionGrid();
      });
    });

    // Solution Filter Tabs
    document.querySelectorAll('.sol-filter').forEach(tab => {
      tab.addEventListener('click', (e) => {
        document.querySelectorAll('.sol-filter').forEach(t => t.classList.remove('active'));
        e.target.classList.add('active');
        state.solutionFilter = e.target.dataset.filter;
        renderSolutions();
      });
    });

    // Submit Modals
    headerSubmitBtn.addEventListener('click', openSubmitModal);
    sidebarSubmitBtn.addEventListener('click', openSubmitModal);
    cancelSubmitBtn.addEventListener('click', closeSubmitModal);
    confirmSubmitBtn.addEventListener('click', submitExam);

    // WhatsApp Share Buttons
    shareWhatsappHeaderBtn.addEventListener('click', shareMockTestWhatsapp);
    if (whatsappShareResultBtn) {
      whatsappShareResultBtn.addEventListener('click', shareResultWhatsapp);
    }

    retakeTestBtn.addEventListener('click', retakeExam);
  }

  // Start Exam
  function startExam() {
    state.candidateName = candidateNameInput.value.trim() || 'Candidate';
    state.isStarted = true;
    state.startTime = Date.now();
    state.timeRemaining = EXAM_DURATION_SECONDS;
    
    // Switch Views
    homeView.classList.remove('active');
    examView.classList.add('active');
    examHeaderTools.classList.remove('hidden');

    startTimer();
    goToPage(1);
    saveState();
  }

  // Resume Exam if page reloaded
  function resumeExam() {
    homeView.classList.remove('active');
    examView.classList.add('active');
    examHeaderTools.classList.remove('hidden');

    startTimer();
    goToPage(state.currentPage || 1);
  }

  // Countdown Timer
  function startTimer() {
    if (timerInterval) clearInterval(timerInterval);

    updateTimerDisplay();

    timerInterval = setInterval(() => {
      state.timeRemaining--;

      if (state.timeRemaining <= 0) {
        clearInterval(timerInterval);
        state.timeRemaining = 0;
        updateTimerDisplay();
        alert('Time is up! Your exam will now be automatically submitted.');
        submitExam();
      } else {
        updateTimerDisplay();
        // Periodic save every 15s
        if (state.timeRemaining % 15 === 0) saveState();
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const hours = Math.floor(state.timeRemaining / 3600);
    const minutes = Math.floor((state.timeRemaining % 3600) / 60);
    const seconds = state.timeRemaining % 60;

    const formatted = 
      String(hours).padStart(2, '0') + ':' + 
      String(minutes).padStart(2, '0') + ':' + 
      String(seconds).padStart(2, '0');

    timerDisplay.textContent = formatted;

    if (state.timeRemaining <= 300) { // 5 minutes
      timerBox.classList.add('timer-urgent');
    } else if (state.timeRemaining <= 1800) { // 30 minutes
      timerDisplay.style.color = '#ea580c';
    }
  }

  // Pagination & Navigation
  function goToPage(pageNumber, scrollToQuestionId = null) {
    if (pageNumber < 1) pageNumber = 1;
    if (pageNumber > TOTAL_PAGES) pageNumber = TOTAL_PAGES;

    state.currentPage = pageNumber;

    // Mark questions on this page as visited
    const startIndex = (pageNumber - 1) * QUESTIONS_PER_PAGE;
    const endIndex = Math.min(startIndex + QUESTIONS_PER_PAGE, TOTAL_QUESTIONS);
    for (let i = startIndex; i < endIndex; i++) {
      const q = state.questions[i];
      if (q) state.visitedQuestions[q.id] = true;
    }

    renderQuestionsPage(startIndex, endIndex);
    renderPaginationControls();
    renderQuestionGrid();
    updateStatusCounts();
    saveState();

    if (scrollToQuestionId) {
      setTimeout(() => {
        const el = document.getElementById(`qCard_${scrollToQuestionId}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
          el.classList.add('highlighted');
          setTimeout(() => el.classList.remove('highlighted'), 2000);
        }
      }, 50);
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  // Handle Direct Jump to Question Number
  function handleJump() {
    const val = parseInt(jumpInput.value, 10);
    if (isNaN(val) || val < 1 || val > TOTAL_QUESTIONS) {
      alert(`Please enter a valid question number between 1 and ${TOTAL_QUESTIONS}.`);
      return;
    }
    const targetPage = Math.ceil(val / QUESTIONS_PER_PAGE);
    goToPage(targetPage, val);
    jumpInput.value = '';
  }

  // Render 10 Questions for the current page
  function renderQuestionsPage(startIndex, endIndex) {
    currentPageIndicator.textContent = `Page ${state.currentPage} of ${TOTAL_PAGES}`;
    currentQuestionRange.textContent = `(Questions ${startIndex + 1} to ${endIndex})`;

    const pageQuestions = state.questions.slice(startIndex, endIndex);

    let html = '';
    pageQuestions.forEach(q => {
      const chosenOpt = state.userAnswers[q.id];
      const isMarked = !!state.markedForReview[q.id];

      html += `
        <div class="question-card" id="qCard_${q.id}">
          <div class="question-card-header">
            <span class="q-badge">Question ${q.id} of 100</span>
            <div class="q-meta">
              <span class="q-section-pill">${q.section} (${q.topic})</span>
              <span class="q-marks-pill">+1.0, -0.20</span>
            </div>
          </div>

          <div class="question-text-box">
            <p class="q-text-en">${q.question_en}</p>
            <p class="q-text-te telugu-text">${q.question_te}</p>
          </div>

          <div class="options-list">
            ${q.options.map((opt, idx) => {
              const isSelected = (chosenOpt === idx);
              return `
                <label class="option-item ${isSelected ? 'selected' : ''}" data-qid="${q.id}" data-opt="${idx}">
                  <input type="radio" name="opt_q_${q.id}" value="${idx}" ${isSelected ? 'checked' : ''} />
                  <div class="option-content">
                    <div class="option-en"><strong>${opt.label}.</strong> ${opt.text_en}</div>
                    <div class="option-te telugu-text">${opt.text_te}</div>
                  </div>
                </label>
              `;
            }).join('')}
          </div>

          <div class="question-actions">
            <button class="btn btn-clear" data-action="clear" data-qid="${q.id}">Clear Choice</button>
            <button class="btn btn-flag ${isMarked ? 'active' : ''}" data-action="flag" data-qid="${q.id}">
              ${isMarked ? '★ Marked for Review' : '☆ Mark for Review'}
            </button>
          </div>
        </div>
      `;
    });

    questionsContainer.innerHTML = html;

    // Attach listeners to newly rendered question options & actions
    attachQuestionInteractions();
  }

  function attachQuestionInteractions() {
    // Option selection
    questionsContainer.querySelectorAll('.option-item').forEach(item => {
      item.addEventListener('click', (e) => {
        const qId = parseInt(item.dataset.qid, 10);
        const optIdx = parseInt(item.dataset.opt, 10);
        selectOption(qId, optIdx);
      });
    });

    // Action buttons
    questionsContainer.querySelectorAll('.question-actions button').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const qId = parseInt(btn.dataset.qid, 10);
        const action = btn.dataset.action;
        if (action === 'clear') {
          clearChoice(qId);
        } else if (action === 'flag') {
          toggleFlag(qId);
        }
      });
    });
  }

  function selectOption(qId, optIdx) {
    state.userAnswers[qId] = optIdx;
    
    // Update visual radio in DOM
    const card = document.getElementById(`qCard_${qId}`);
    if (card) {
      card.querySelectorAll('.option-item').forEach(el => el.classList.remove('selected'));
      const chosenEl = card.querySelector(`.option-item[data-opt="${optIdx}"]`);
      if (chosenEl) {
        chosenEl.classList.add('selected');
        const radio = chosenEl.querySelector('input[type="radio"]');
        if (radio) radio.checked = true;
      }
    }

    renderQuestionGrid();
    updateStatusCounts();
    saveState();
  }

  function clearChoice(qId) {
    delete state.userAnswers[qId];
    const card = document.getElementById(`qCard_${qId}`);
    if (card) {
      card.querySelectorAll('.option-item').forEach(el => {
        el.classList.remove('selected');
        const radio = el.querySelector('input[type="radio"]');
        if (radio) radio.checked = false;
      });
    }
    renderQuestionGrid();
    updateStatusCounts();
    saveState();
  }

  function toggleFlag(qId) {
    state.markedForReview[qId] = !state.markedForReview[qId];
    const card = document.getElementById(`qCard_${qId}`);
    if (card) {
      const flagBtn = card.querySelector('.btn-flag');
      if (flagBtn) {
        if (state.markedForReview[qId]) {
          flagBtn.classList.add('active');
          flagBtn.textContent = '★ Marked for Review';
        } else {
          flagBtn.classList.remove('active');
          flagBtn.textContent = '☆ Mark for Review';
        }
      }
    }
    renderQuestionGrid();
    updateStatusCounts();
    saveState();
  }

  // Render Bottom Pagination Numbers (Pages 1 to 10)
  function renderPaginationControls() {
    prevPageBtn.disabled = (state.currentPage === 1);
    nextPageBtn.disabled = (state.currentPage === TOTAL_PAGES);

    let html = '';
    for (let p = 1; p <= TOTAL_PAGES; p++) {
      const startQ = (p - 1) * 10 + 1;
      const endQ = p * 10;
      html += `
        <button class="page-btn ${p === state.currentPage ? 'active' : ''}" 
          data-page="${p}" 
          title="Questions ${startQ} to ${endQ}">
          ${p}
        </button>
      `;
    }
    paginationNumbers.innerHTML = html;

    paginationNumbers.querySelectorAll('.page-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const p = parseInt(btn.dataset.page, 10);
        goToPage(p);
      });
    });
  }

  // Render Sidebar Question Grid (1-100 buttons)
  function renderQuestionGrid() {
    let filteredQuestions = state.questions;
    if (state.paletteFilter === 'arithmetic') {
      filteredQuestions = state.questions.filter(q => q.id <= 50);
    } else if (state.paletteFilter === 'reasoning') {
      filteredQuestions = state.questions.filter(q => q.id > 50);
    }

    let html = '';
    filteredQuestions.forEach(q => {
      const isAnswered = state.userAnswers[q.id] !== undefined;
      const isMarked = !!state.markedForReview[q.id];
      const isVisited = !!state.visitedQuestions[q.id];

      let statusClass = 'not-visited';
      if (isMarked) {
        statusClass = 'marked';
      } else if (isAnswered) {
        statusClass = 'answered';
      } else if (isVisited) {
        statusClass = 'unanswered';
      }

      html += `
        <button class="pal-btn ${statusClass}" data-qid="${q.id}" title="Q${q.id}: ${statusClass}">
          ${q.id}
        </button>
      `;
    });

    questionGrid.innerHTML = html;

    questionGrid.querySelectorAll('.pal-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const qId = parseInt(btn.dataset.qid, 10);
        const targetPage = Math.ceil(qId / QUESTIONS_PER_PAGE);
        goToPage(targetPage, qId);
      });
    });
  }

  // Update Status Legend Counters
  function updateStatusCounts() {
    let answered = 0;
    let marked = 0;
    let visited = 0;

    for (let i = 1; i <= TOTAL_QUESTIONS; i++) {
      if (state.markedForReview[i]) marked++;
      if (state.userAnswers[i] !== undefined) answered++;
      if (state.visitedQuestions[i]) visited++;
    }

    const notVisited = TOTAL_QUESTIONS - visited;
    const unanswered = TOTAL_QUESTIONS - answered;

    countAnswered.textContent = answered;
    countUnanswered.textContent = unanswered;
    countMarked.textContent = marked;
    countNotVisited.textContent = notVisited;

    modalAnswered.textContent = answered;
    modalUnanswered.textContent = unanswered;
    modalMarked.textContent = marked;
  }

  // Modal handlers
  function openSubmitModal() {
    updateStatusCounts();
    submitModal.classList.remove('hidden');
  }

  function closeSubmitModal() {
    submitModal.classList.add('hidden');
  }

  // Submit Exam & Calculate Scores
  function submitExam() {
    if (timerInterval) clearInterval(timerInterval);
    closeSubmitModal();

    state.isSubmitted = true;
    state.endTime = Date.now();
    saveState();

    showResults();
  }

  function showResults() {
    examView.classList.remove('active');
    examHeaderTools.classList.add('hidden');
    resultView.classList.add('active');

    // Compute metrics
    let correct = 0;
    let wrong = 0;
    let unattempted = 0;

    // Sectional Breakdown
    let arithTotal = 50, arithAttempted = 0, arithCorrect = 0, arithWrong = 0;
    let reasTotal = 50, reasAttempted = 0, reasCorrect = 0, reasWrong = 0;

    state.questions.forEach(q => {
      const userChoice = state.userAnswers[q.id];
      const isArith = (q.id <= 50);

      if (userChoice === undefined) {
        unattempted++;
      } else {
        if (isArith) arithAttempted++; else reasAttempted++;

        if (userChoice === q.correct_answer) {
          correct++;
          if (isArith) arithCorrect++; else reasCorrect++;
        } else {
          wrong++;
          if (isArith) arithWrong++; else reasWrong++;
        }
      }
    });

    const netScore = Math.max(0, (correct * 1.0) - (wrong * NEGATIVE_MARK));
    const totalAttempted = correct + wrong;
    const accuracy = totalAttempted > 0 ? ((correct / totalAttempted) * 100).toFixed(1) : '0.0';
    const percentage = ((netScore / TOTAL_QUESTIONS) * 100).toFixed(2);

    // Time taken
    const secondsSpent = EXAM_DURATION_SECONDS - state.timeRemaining;
    const hours = Math.floor(secondsSpent / 3600);
    const mins = Math.floor((secondsSpent % 3600) / 60);
    const secs = secondsSpent % 60;
    const timeSpentFormatted = `${String(hours).padStart(2,'0')}:${String(mins).padStart(2,'0')}:${String(secs).padStart(2,'0')}`;

    // Fill UI
    document.getElementById('resultCandidateName').textContent = `${state.candidateName} - TSPLRB SI Prelims Scorecard`;
    document.getElementById('resultTimestamp').textContent = `Submitted on ${new Date().toLocaleString()}`;

    document.getElementById('resFinalScore').textContent = `${netScore.toFixed(2)} / 100`;
    document.getElementById('resPercentage').textContent = `${percentage}% Net Marks`;
    document.getElementById('resCorrect').textContent = correct;
    document.getElementById('resWrong').textContent = wrong;
    document.getElementById('resUnattempted').textContent = unattempted;
    document.getElementById('resAccuracy').textContent = `${accuracy}%`;
    document.getElementById('resTimeTaken').textContent = timeSpentFormatted;

    // Section table
    const arithScore = Math.max(0, arithCorrect * 1.0 - arithWrong * NEGATIVE_MARK);
    const arithAcc = arithAttempted > 0 ? ((arithCorrect / arithAttempted) * 100).toFixed(1) : '0.0';
    const reasScore = Math.max(0, reasCorrect * 1.0 - reasWrong * NEGATIVE_MARK);
    const reasAcc = reasAttempted > 0 ? ((reasCorrect / reasAttempted) * 100).toFixed(1) : '0.0';

    const sectionBody = document.getElementById('sectionSummaryBody');
    sectionBody.innerHTML = `
      <tr>
        <td><strong>Part A: Arithmetic (అంకగణితం)</strong></td>
        <td>${arithTotal}</td>
        <td>${arithAttempted}</td>
        <td style="color:#16a34a; font-weight:700;">${arithCorrect}</td>
        <td style="color:#dc2626; font-weight:700;">${arithWrong}</td>
        <td><strong>${arithScore.toFixed(2)}</strong></td>
        <td>${arithAcc}%</td>
      </tr>
      <tr>
        <td><strong>Part B: Reasoning & Mental Ability (రీజనింగ్)</strong></td>
        <td>${reasTotal}</td>
        <td>${reasAttempted}</td>
        <td style="color:#16a34a; font-weight:700;">${reasCorrect}</td>
        <td style="color:#dc2626; font-weight:700;">${reasWrong}</td>
        <td><strong>${reasScore.toFixed(2)}</strong></td>
        <td>${reasAcc}%</td>
      </tr>
      <tr style="background:#f8fafc; font-weight:800;">
        <td>Total</td>
        <td>100</td>
        <td>${totalAttempted}</td>
        <td style="color:#16a34a;">${correct}</td>
        <td style="color:#dc2626;">${wrong}</td>
        <td style="color:#1d4ed8; font-size:1.05rem;">${netScore.toFixed(2)} / 100</td>
        <td>${accuracy}%</td>
      </tr>
    `;

    renderSolutions();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Render Solutions & Explanations
  function renderSolutions() {
    const list = document.getElementById('solutionsList');
    if (!list) return;

    let filtered = state.questions;
    if (state.solutionFilter === 'correct') {
      filtered = state.questions.filter(q => state.userAnswers[q.id] === q.correct_answer);
    } else if (state.solutionFilter === 'wrong') {
      filtered = state.questions.filter(q => {
        const a = state.userAnswers[q.id];
        return a !== undefined && a !== q.correct_answer;
      });
    } else if (state.solutionFilter === 'unattempted') {
      filtered = state.questions.filter(q => state.userAnswers[q.id] === undefined);
    }

    if (filtered.length === 0) {
      list.innerHTML = `<p style="text-align:center; padding:2rem; color:#64748b;">No questions match the "${state.solutionFilter}" filter.</p>`;
      return;
    }

    let html = '';
    filtered.forEach(q => {
      const userChoice = state.userAnswers[q.id];
      const isUnattempted = (userChoice === undefined);
      const isCorrect = (userChoice === q.correct_answer);

      let cardClass = 'is-unattempted';
      let tagHtml = '<span class="sol-status-tag tag-unattempted">Unattempted (0.00)</span>';

      if (!isUnattempted) {
        if (isCorrect) {
          cardClass = 'is-correct';
          tagHtml = '<span class="sol-status-tag tag-correct">Correct (+1.00)</span>';
        } else {
          cardClass = 'is-wrong';
          tagHtml = '<span class="sol-status-tag tag-wrong">Incorrect (-0.20)</span>';
        }
      }

      html += `
        <div class="sol-card ${cardClass}">
          <div class="sol-card-header">
            <strong>Question ${q.id} &bull; ${q.section} (${q.topic})</strong>
            ${tagHtml}
          </div>

          <p class="q-text-en">${q.question_en}</p>
          <p class="q-text-te telugu-text">${q.question_te}</p>

          <div class="sol-options-breakdown">
            ${q.options.map((opt, idx) => {
              const isActualCorrect = (idx === q.correct_answer);
              const isUserChoice = (idx === userChoice);

              let optClass = '';
              let badge = '';

              if (isActualCorrect) {
                optClass = 'opt-correct';
                badge = ' [Official Key]';
              } else if (isUserChoice && !isCorrect) {
                optClass = 'opt-chosen-wrong';
                badge = ' [Your Answer - Incorrect]';
              }

              return `
                <div class="sol-opt-row ${optClass}">
                  <span><strong>${opt.label}.</strong> ${opt.text_en} / ${opt.text_te}</span>
                  <span><strong>${badge}</strong></span>
                </div>
              `;
            }).join('')}
          </div>

          <div class="sol-explanation-box">
            <strong>Detailed Solution / వివరణ:</strong>
            <p>${q.explanation_en}</p>
            <p class="exp-te telugu-text">${q.explanation_te}</p>
          </div>
        </div>
      `;
    });

    list.innerHTML = html;
  }

  // WhatsApp Sharing
  function shareMockTestWhatsapp() {
    const currentUrl = window.location.href.split('#')[0];
    const text = encodeURIComponent(
      `🚨 *TSPLRB SI Prelims Daily Mock Test Series 2026* 🚨\n\n` +
      `Prepare for upcoming Telangana Police Sub-Inspector (SI) Preliminary Exam with authentic full-length practice tests!\n\n` +
      `📝 *Exam Details:*\n` +
      `• 100 Questions (50 Arithmetic + 50 Reasoning)\n` +
      `• Bilingual (English & Telugu)\n` +
      `• 3 Hours Real CBT Timer\n` +
      `• Negative Marking (-0.20) & Instant Detailed Solutions\n\n` +
      `👉 Click here to start test now:\n${currentUrl}`
    );
    window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
  }

  function shareResultWhatsapp() {
    const currentUrl = window.location.href.split('#')[0];
    const score = document.getElementById('resFinalScore').textContent;
    const accuracy = document.getElementById('resAccuracy').textContent;
    const correct = document.getElementById('resCorrect').textContent;
    const wrong = document.getElementById('resWrong').textContent;

    const text = encodeURIComponent(
      `🎯 *TSPLRB SI Prelims Mock Test 01 Result* 🎯\n` +
      `Candidate: *${state.candidateName}*\n\n` +
      `🏆 *Final Score:* ${score}\n` +
      `✅ *Correct Answers:* ${correct}\n` +
      `❌ *Wrong Answers:* ${wrong}\n` +
      `🎯 *Accuracy:* ${accuracy}\n\n` +
      `Can you beat my score? Take the daily mock test here:\n${currentUrl}`
    );
    window.open(`https://api.whatsapp.com/send?text=${text}`, '_blank');
  }

  // Retake Exam
  function retakeExam() {
    if (confirm('Are you sure you want to retake the exam? Your previous responses will be cleared.')) {
      localStorage.removeItem(STORAGE_KEY);
      window.location.reload();
    }
  }

  // Local Storage Save / Load
  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        candidateName: state.candidateName,
        currentPage: state.currentPage,
        userAnswers: state.userAnswers,
        markedForReview: state.markedForReview,
        visitedQuestions: state.visitedQuestions,
        timeRemaining: state.timeRemaining,
        isStarted: state.isStarted,
        isSubmitted: state.isSubmitted,
        startTime: state.startTime,
        endTime: state.endTime
      }));
    } catch (e) {
      console.warn('Could not save state to localStorage', e);
    }
  }

  function loadSavedState() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        state = { ...state, ...parsed };
      }
    } catch (e) {
      console.warn('Could not parse saved state', e);
    }
  }

  // Bootstrap when DOM ready
  document.addEventListener('DOMContentLoaded', init);
})();
