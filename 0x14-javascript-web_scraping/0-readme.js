#!/usr/bin/node

const argv = process.argv.slice(2);
const filename = argv[0];

const fs = require('fs');

fs.readFile(filename, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
