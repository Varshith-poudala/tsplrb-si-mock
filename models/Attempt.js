import mongoose from 'mongoose';

const AttemptSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
    index: true,
  },
  userEmail: {
    type: String,
    required: true,
    index: true,
  },
  testId: {
    type: String,
    required: true,
    index: true,
  },
  attemptNumber: {
    type: Number,
    default: 1,
  },
  startedAt: {
    type: Date,
    required: true,
  },
  submittedAt: {
    type: Date,
    default: Date.now,
  },
  durationSeconds: {
    type: Number,
    default: 0,
  },
  totalScore: {
    type: Number,
    required: true,
  },
  totalMarks: {
    type: Number,
    default: 200,
  },
  correctCount: {
    type: Number,
    default: 0,
  },
  wrongCount: {
    type: Number,
    default: 0,
  },
  unansweredCount: {
    type: Number,
    default: 0,
  },
  accuracyPercent: {
    type: Number,
    default: 0,
  },
  sectionScores: {
    type: mongoose.Schema.Types.Mixed,
    default: {},
  },
  answers: [
    {
      qNumber: Number,
      selectedOption: Number, // null if unanswered
      isCorrect: Boolean,
      correctOption: Number,
    }
  ],
  createdAt: {
    type: Date,
    default: Date.now,
    index: true,
  }
});

export default mongoose.models.Attempt || mongoose.model('Attempt', AttemptSchema);
