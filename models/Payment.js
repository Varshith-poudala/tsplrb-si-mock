import mongoose from 'mongoose';

const PaymentSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
  },
  userEmail: {
    type: String,
    required: true,
    index: true,
  },
  userPhone: {
    type: String,
    default: '',
  },
  amount: {
    type: Number,
    required: true,
  },
  currency: {
    type: String,
    default: 'INR',
  },
  gateway: {
    type: String,
    enum: ['razorpay', 'upi_utr', 'admin_manual', 'free_promo'],
    default: 'razorpay',
  },
  transactionId: {
    type: String,
    required: true,
    unique: true,
  },
  orderId: {
    type: String,
    default: '',
  },
  utrNumber: {
    type: String,
    default: '',
  },
  status: {
    type: String,
    enum: ['pending', 'completed', 'failed', 'refunded'],
    default: 'pending',
  },
  adminGrantedBy: {
    type: String,
    default: '',
  },
  createdAt: {
    type: Date,
    default: Date.now,
  }
});

export default mongoose.models.Payment || mongoose.model('Payment', PaymentSchema);
