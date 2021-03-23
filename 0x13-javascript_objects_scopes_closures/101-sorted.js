#!/usr/bin/node

const dict = require('./101-data.js').dict;

const ndict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!ndict[value]) ndict[value] = [key];
  else ndict[value].push(key);
}

console.log(ndict);
