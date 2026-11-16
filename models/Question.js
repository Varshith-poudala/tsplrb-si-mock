import mongoose from 'mongoose';

const QuestionSchema = new mongoose.Schema({
  testId: {
    type: String,
    required: true,
    index: true,
  },
  qNumber: {
    type: Number,
    required: true,
  },
  section: {
    type: String,
    required: true,
  },
  topic: {
    type: String,
    default: '',
  },
  question_en: {
    type: String,
    required: true,
  },
  question_te: {
    type: String,
    required: true,
  },
  options_en: {
    type: [String],
    required: true,
  },
  options_te: {
    type: [String],
    required: true,
  },
  correct_option: {
    type: Number,
    required: true,
  },
  explanation_en: {
    type: String,
    default: '',
  },
  explanation_te: {
    type: String,
    default: '',
  }
});

QuestionSchema.index({ testId: 1, qNumber: 1 }, { unique: true });

export default mongoose.models.Question || mongoose.model('Question', QuestionSchema);
