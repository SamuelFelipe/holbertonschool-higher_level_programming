#!/usr/bin/node

const argv = process.argv.slice(2);
const url = argv[0];
const filename = argv[1];

const fs = require('fs');
const request = require('request');
let data;

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  data = body;
  fs.writeFile(filename, data, 'utf-8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
