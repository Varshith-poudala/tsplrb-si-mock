import { spawn } from 'child_process';
import dotenv from 'dotenv';
dotenv.config({ path: '.env.local' });

console.log('🚀 Starting TSPLRB SI Vite + React Development Environment...');

// 1. Start Express API Backend (Port 5000) with auto-reload
const server = spawn('node', ['--watch', 'server/index.js'], {
  stdio: 'inherit',
  shell: true,
  env: process.env,
});

// 2. Start Vite Frontend Server (Port 3000)
const client = spawn('npx', ['vite', '--port', '3000', '--host'], {
  stdio: 'inherit',
  shell: true,
  env: process.env,
});

process.on('SIGINT', () => {
  try { server.kill(); } catch (e) {}
  try { client.kill(); } catch (e) {}
  process.exit(0);
});

process.on('SIGTERM', () => {
  try { server.kill(); } catch (e) {}
  try { client.kill(); } catch (e) {}
  process.exit(0);
});
