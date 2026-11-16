import GoogleProvider from 'next-auth/providers/google';
import CredentialsProvider from 'next-auth/providers/credentials';
import connectToDatabase from './mongodb';
import User from '@/models/User';

export const authOptions = {
  providers: [
    // 1. Google OAuth Provider
    ...(process.env.GOOGLE_CLIENT_ID && process.env.GOOGLE_CLIENT_SECRET
      ? [
          GoogleProvider({
            clientId: process.env.GOOGLE_CLIENT_ID,
            clientSecret: process.env.GOOGLE_CLIENT_SECRET,
          }),
        ]
      : []),

    // 2. Fast Dev / Direct Login Provider (for local testing & instant admin access without waiting for Google Console keys)
    CredentialsProvider({
      id: 'dev-login',
      name: 'Direct Access',
      credentials: {
        email: { label: 'Email', type: 'email', placeholder: 'your@email.com' },
        name: { label: 'Name', type: 'text' },
      },
      async authorize(credentials) {
        if (!credentials?.email) return null;
        return {
          id: credentials.email,
          email: credentials.email.toLowerCase(),
          name: credentials.name || credentials.email.split('@')[0],
          image: '',
        };
      },
    }),
  ],

  callbacks: {
    async signIn({ user }) {
      try {
        const conn = await connectToDatabase();
        const email = user.email.toLowerCase();
        const adminEmails = (process.env.ADMIN_EMAILS || 'varshithpoudala@gmail.com')
          .toLowerCase()
          .split(',')
          .map(e => e.trim());

        const isAdmin = adminEmails.includes(email);

        if (conn) {
          // Find or create user in DB
          let dbUser = await User.findOne({ email });
          if (!dbUser) {
            dbUser = await User.create({
              email,
              name: user.name || 'Candidate',
              image: user.image || '',
              role: isAdmin ? 'admin' : 'user',
              isPaid: isAdmin ? true : false,
              accessGrantedBy: isAdmin ? 'admin' : null,
              accessGrantedAt: isAdmin ? new Date() : null,
            });
          } else {
            if (isAdmin) {
              dbUser.role = 'admin';
              dbUser.isPaid = true;
              if (!dbUser.accessGrantedBy) dbUser.accessGrantedBy = 'admin';
              await dbUser.save();
            }
          }
        }
        return true;
      } catch (err) {
        console.error('Sign-in error:', err);
        return true;
      }
    },

    async session({ session }) {
      if (session?.user?.email) {
        const email = session.user.email.toLowerCase();
        const adminEmails = (process.env.ADMIN_EMAILS || 'varshithpoudala@gmail.com')
          .toLowerCase()
          .split(',')
          .map(e => e.trim());

        const isAdmin = adminEmails.includes(email);

        try {
          const conn = await connectToDatabase();
          if (conn) {
            const dbUser = await User.findOne({ email });
            if (dbUser) {
              session.user.id = dbUser._id.toString();
              session.user.role = dbUser.role || (isAdmin ? 'admin' : 'user');
              session.user.isPaid = dbUser.isPaid || isAdmin;
              session.user.accessGrantedBy = dbUser.accessGrantedBy;
            } else {
              session.user.role = isAdmin ? 'admin' : 'user';
              session.user.isPaid = isAdmin;
            }
          } else {
            session.user.role = isAdmin ? 'admin' : 'user';
            session.user.isPaid = isAdmin;
          }
        } catch {
          session.user.role = isAdmin ? 'admin' : 'user';
          session.user.isPaid = isAdmin;
        }
      }
      return session;
    },

    async jwt({ token, user }) {
      if (user) {
        token.email = user.email;
        token.name = user.name;
      }
      return token;
    },
  },

  session: {
    strategy: 'jwt',
  },
  secret: process.env.NEXTAUTH_SECRET || 'tsplrb_secret_development_session_key_9999',
  pages: {
    signIn: '/login',
  },
};
