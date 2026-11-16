import nodemailer from 'nodemailer';

/**
 * Creates and caches the nodemailer transporter using environment variables.
 * Supports Gmail (with App Passwords), Brevo, SendGrid, Amazon SES, or any standard SMTP.
 */
let cachedTransporter = null;

export function getTransporter() {
  const host = process.env.SMTP_HOST || (process.env.GMAIL_USER ? 'smtp.gmail.com' : null);
  const port = parseInt(process.env.SMTP_PORT || '587', 10);
  const user = process.env.SMTP_USER || process.env.GMAIL_USER;
  const pass = (process.env.SMTP_PASS || process.env.GMAIL_APP_PASSWORD || '').replace(/\s+/g, '');
  const secure = process.env.SMTP_SECURE === 'true' || port === 465;

  if (!user || !pass) {
    return null;
  }

  // Create transporter
  return nodemailer.createTransport({
    host: host || 'smtp.gmail.com',
    port,
    secure,
    auth: {
      user,
      pass,
    },
    // Useful for local testing with self-signed certs
    tls: {
      rejectUnauthorized: process.env.NODE_ENV === 'production',
    },
  });
}

/**
 * Checks whether email delivery is configured in environment variables.
 * Supports Resend API (RESEND_API_KEY) or standard SMTP (SMTP_USER + SMTP_PASS).
 */
export function isEmailConfigured() {
  const hasResend = Boolean(process.env.RESEND_API_KEY);
  const user = process.env.SMTP_USER || process.env.GMAIL_USER;
  const pass = (process.env.SMTP_PASS || process.env.GMAIL_APP_PASSWORD || '').replace(/\s+/g, '');
  const hasSmtp = Boolean(user && pass);
  return hasResend || hasSmtp;
}

/**
 * Sends a high-priority 6-digit OTP email for password recovery.
 */
export async function sendPasswordResetEmail({ to, name = 'Candidate', resetCode }) {
  const htmlContent = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Reset Your Password - TSPLRB SI Mock Test Series</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f8fafc; color: #1e293b; margin: 0; padding: 24px; }
    .container { max-width: 520px; margin: 0 auto; background: #ffffff; border-radius: 16px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
    .header { background: #0f172a; padding: 24px; text-align: center; color: #ffffff; }
    .header h1 { margin: 0; font-size: 18px; font-weight: 800; letter-spacing: -0.02em; }
    .header p { margin: 4px 0 0; font-size: 12px; color: #94a3b8; }
    .content { padding: 32px 28px; }
    .greeting { font-size: 15px; font-weight: 600; margin-bottom: 12px; }
    .instruction { font-size: 13px; line-height: 1.6; color: #475569; margin-bottom: 24px; }
    .otp-card { background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 20px; text-align: center; margin: 24px 0; }
    .otp-code { font-family: monospace; font-size: 32px; font-weight: 900; letter-spacing: 6px; color: #1e40af; margin: 0; }
    .otp-expiry { font-size: 11px; color: #64748b; margin-top: 8px; }
    .security-note { font-size: 12px; color: #64748b; line-height: 1.5; border-top: 1px solid #f1f5f9; padding-top: 16px; margin-top: 24px; }
    .footer { background: #f8fafc; padding: 16px; text-align: center; font-size: 11px; color: #94a3b8; border-top: 1px solid #e2e8f0; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>TSPLRB SI Mock Test Series</h1>
      <p>Sub-Inspector Preliminary Written Test (PWT) 2024-25</p>
    </div>
    <div class="content">
      <div class="greeting">Hello ${name || 'Candidate'},</div>
      <div class="instruction">
        We received a request to reset the password for your TSPLRB SI Exam account (<strong>${to}</strong>).
        Use the 6-digit verification code below to authorize your new password:
      </div>

      <div class="otp-card">
        <div class="otp-code">${resetCode}</div>
        <div class="otp-expiry">Valid for 15 minutes • Single use only</div>
      </div>

      <div class="security-note">
        <strong>Security Notice:</strong> If you did not request this password reset, please ignore this email. Your current password will remain unchanged and your account is secure.
      </div>
    </div>
    <div class="footer">
      TSPLRB SI CBT Examination Preparation Portal • All Rights Reserved
    </div>
  </div>
</body>
</html>
  `;

  const textContent = `
Hello ${name || 'Candidate'},

We received a request to reset your password for the TSPLRB SI Mock Test Series (${to}).

Your 6-Digit Password Reset Code is:
${resetCode}

This code is valid for 15 minutes.
If you did not request this code, you can safely ignore this email.

TSPLRB SI CBT Portal
  `.trim();

  const subject = `[TSPLRB SI] Your Password Reset Code: ${resetCode}`;

  // 1. Resend API Dispatch (if configured)
  if (process.env.RESEND_API_KEY) {
    const fromAddress = process.env.EMAIL_FROM || process.env.RESEND_FROM || 'TSPLRB SI Prep <onboarding@resend.dev>';
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: fromAddress,
        to: [to],
        subject,
        html: htmlContent,
        text: textContent,
      }),
    });

    const data = await res.json();
    if (!res.ok) {
      console.error('❌ Resend API error:', data);
      throw new Error(data.message || 'Resend email delivery failed');
    }
    console.log(`📧 [Resend] Password reset email sent successfully to ${to} (ID: ${data.id})`);
    return { success: true, messageId: data.id };
  }

  // 2. SMTP Dispatch via Nodemailer (if configured)
  const transporter = getTransporter();

  if (!transporter) {
    console.error('❌ [Mailer Error] Neither RESEND_API_KEY nor SMTP credentials set in .env.local! Cannot dispatch email to', to);
    throw new Error('Email service is not configured. Please add RESEND_API_KEY or SMTP_USER and SMTP_PASS in .env.local.');
  }

  const fromAddress = process.env.SMTP_FROM || `TSPLRB SI Mock Test Series <${process.env.SMTP_USER || process.env.GMAIL_USER}>`;

  const mailOptions = {
    from: fromAddress,
    to,
    subject,
    text: textContent,
    html: htmlContent,
  };

  const info = await transporter.sendMail(mailOptions);
  console.log(`📧 [Mailer] Password reset email sent successfully to ${to} (MessageId: ${info.messageId})`);
  return { success: true, messageId: info.messageId };
}
