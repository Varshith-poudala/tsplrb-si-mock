/**
 * TSPLRB SI Prelims Daily Mock Test Server
 * High performance static server with local IP detection for WhatsApp sharing.
 * Zero external dependencies (uses standard Node.js library).
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const os = require('os');

const PORT = process.env.PORT || 3000;
const PUBLIC_DIR = path.join(__dirname, 'public');

const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.js': 'application/javascript; charset=UTF-8',
  '.json': 'application/json; charset=UTF-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf'
};

// Find local IPv4 address for local network / WhatsApp sharing
function getLocalIpAddresses() {
  const interfaces = os.networkInterfaces();
  const addresses = [];
  for (const name of Object.keys(interfaces)) {
    for (const net of interfaces[name]) {
      // Skip internal (i.e. 127.0.0.1) and non-ipv4 addresses
      if (net.family === 'IPv4' && !net.internal) {
        addresses.push({ iface: name, ip: net.address });
      }
    }
  }
  return addresses;
}

const server = http.createServer((req, res) => {
  // Normalize URL
  let safeUrl = req.url.split('?')[0];
  if (safeUrl === '/') {
    safeUrl = '/index.html';
  }

  // Prevent directory traversal
  const filePath = path.normalize(path.join(PUBLIC_DIR, safeUrl));
  if (!filePath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found');
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    // Set caching and security headers
    res.writeHead(200, {
      'Content-Type': contentType,
      'Access-Control-Allow-Origin': '*',
      'Cache-Control': ext === '.json' || ext === '.html' ? 'no-cache' : 'public, max-age=86400'
    });

    const stream = fs.createReadStream(filePath);
    stream.pipe(res);
  });
});

server.listen(PORT, '0.0.0.0', () => {
  const localIps = getLocalIpAddresses();
  console.log('================================================================');
  console.log('🚀 TSPLRB SI Prelims Daily Mock Test Portal is running!');
  console.log('================================================================');
  console.log(`📱 Local access:   http://localhost:${PORT}`);
  
  if (localIps.length > 0) {
    console.log('\n📲 Share this link on WhatsApp for anyone on your Wi-Fi/Hotspot:');
    localIps.forEach(({ iface, ip }) => {
      console.log(`   👉 http://${ip}:${PORT}  (${iface})`);
    });
  } else {
    console.log(`\n📲 Shareable link: http://localhost:${PORT}`);
  }

  console.log('\n🌐 For global public sharing over internet:');
  console.log(`   - Option 1 (Cloudflare Tunnel): npx cloudflared tunnel --url http://localhost:${PORT}`);
  console.log(`   - Option 2 (Localtunnel):       npx localtunnel --port ${PORT}`);
  console.log(`   - Option 3 (Ngrok):             ngrok http ${PORT}`);
  console.log('================================================================\n');
});
