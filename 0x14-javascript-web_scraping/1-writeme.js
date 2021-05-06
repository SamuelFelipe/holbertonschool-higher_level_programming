#!/usr/bin/node

const argv = process.argv.slice(2);
const filename = argv[0];
const data = argv[1];

const fs = require('fs');

fs.writeFile(filename, argv[1], 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
