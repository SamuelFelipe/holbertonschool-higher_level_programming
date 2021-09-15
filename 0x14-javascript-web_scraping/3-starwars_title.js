#!/usr/bin/node

const argv = process.argv.slice(2);
const id = argv[0];

const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  const info = JSON.parse(body);
  console.log(info.title);
});
