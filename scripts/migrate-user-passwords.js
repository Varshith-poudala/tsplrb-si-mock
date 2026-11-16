import dotenv from 'dotenv';
dotenv.config({ path: '.env.local' });
import connectToDatabase from '../lib/mongodb.js';
import User from '../models/User.js';
import { hashPassword } from '../lib/crypto-auth.js';

async function migrateExistingUserPasswords() {
  console.log('🔄 Connecting to MongoDB to migrate user passwords to default "12345678"...');
  await connectToDatabase();

  const DEFAULT_PASSWORD = '12345678';
  const users = await User.find({});

  console.log(`Found ${users.length} user(s) to migrate.`);

  for (const user of users) {
    const { hash, salt } = hashPassword(DEFAULT_PASSWORD);
    user.passwordHash = hash;
    user.salt = salt;
    await user.save();
    console.log(`✅ Set password "12345678" for ${user.email} (Role: ${user.role}, Paid: ${user.isPaid})`);
  }

  console.log('🎉 Password migration completed successfully for all users!');
  process.exit(0);
}

migrateExistingUserPasswords().catch(err => {
  console.error('Migration failed:', err);
  process.exit(1);
});
