import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true,
  },
  name: {
    type: String,
    default: 'Candidate',
  },
  passwordHash: {
    type: String,
    default: '',
  },
  salt: {
    type: String,
    default: '',
  },
  resetCode: {
    type: String,
    default: null,
  },
  resetCodeExpires: {
    type: Date,
    default: null,
  },
  image: {
    type: String,
    default: '',
  },
  phone: {
    type: String,
    default: '',
  },
  role: {
    type: String,
    enum: ['user', 'admin'],
    default: 'user',
  },
  isPaid: {
    type: Boolean,
    default: false,
  },
  accessGrantedBy: {
    type: String,
    enum: ['payment', 'admin', 'free_demo', 'promo', null],
    default: null,
  },
  accessGrantedAt: {
    type: Date,
    default: null,
  },
  notes: {
    type: String,
    default: '',
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
  lastLoginAt: {
    type: Date,
    default: Date.now,
  }
});

export default mongoose.models.User || mongoose.model('User', UserSchema);
