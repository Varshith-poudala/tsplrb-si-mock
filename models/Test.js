import mongoose from 'mongoose';

const TestSchema = new mongoose.Schema({
  testId: {
    type: String,
    required: true,
    unique: true,
  },
  title: {
    type: String,
    required: true,
  },
  title_te: {
    type: String,
    default: '',
  },
  exam: {
    type: String,
    default: 'TSPLRB SI Preliminary Written Test',
  },
  totalQuestions: {
    type: Number,
    required: true,
    default: 200,
  },
  totalMarks: {
    type: Number,
    required: true,
    default: 200,
  },
  durationMinutes: {
    type: Number,
    required: true,
    default: 180,
  },
  marksPerQuestion: {
    type: Number,
    default: 1.0,
  },
  negativeMarking: {
    type: Number,
    default: 0.20,
  },
  isFreeDemo: {
    type: Boolean,
    default: false,
  },
  isActive: {
    type: Boolean,
    default: true,
  },
  sections: [
    {
      id: String,
      name: String,
      start: Number,
      end: Number,
      count: Number,
    }
  ],
  createdAt: {
    type: Date,
    default: Date.now,
  }
});

export default mongoose.models.Test || mongoose.model('Test', TestSchema);
