#!/usr/bin/node

const argv = process.argv.slice(2);
const url = argv[0];

const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const info = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < info.count; i++) {
    info.results[i].characters.forEach(character => {
      if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    });
  }
  console.log(count);
});
