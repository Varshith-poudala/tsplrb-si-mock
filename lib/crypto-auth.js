import crypto from 'crypto';

/**
 * Derives a cryptographic hash from a password and salt using scrypt.
 */
export function hashPassword(password, salt = crypto.randomBytes(16).toString('hex')) {
  const hash = crypto.scryptSync(password, salt, 64).toString('hex');
  return { hash, salt };
}

/**
 * Verifies a password against a stored scrypt hash and salt in constant time.
 */
export function verifyPassword(password, hash, salt) {
  if (!password || !hash || !salt) return false;
  try {
    const computedHash = crypto.scryptSync(password, salt, 64).toString('hex');
    const hashBuf = Buffer.from(hash, 'hex');
    const computedBuf = Buffer.from(computedHash, 'hex');
    if (hashBuf.length !== computedBuf.length) return false;
    return crypto.timingSafeEqual(hashBuf, computedBuf);
  } catch (err) {
    console.error('verifyPassword error:', err);
    return false;
  }
}
