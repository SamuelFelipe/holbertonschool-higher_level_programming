#!/usr/bin/node

const argv = process.argv.slice(2);
const url = argv[0];

const https = require('https');

const req = https.request(url, 'GET', res => {
  console.log(`code: ${res.statusCode}`);
});

req.end();
