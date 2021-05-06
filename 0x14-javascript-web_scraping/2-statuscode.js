#!/usr/bin/node

const argv = process.argv.slice(2);
const url = argv[0];

const req = require('request');

req.get(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
