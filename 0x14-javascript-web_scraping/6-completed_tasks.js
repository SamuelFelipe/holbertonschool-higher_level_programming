#!/usr/bin/node

const argv = process.argv.slice(2);
const url = argv[0];

const request = require('request');
const data = {};
let users;

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  users = JSON.parse(body);

  for (let i = 0; i < users.length; i++) {
    if (users[i].completed === true) {
      if (data[users[i].userId]) {
        data[users[i].userId] += 1;
      } else {
        data[users[i].userId] = 1;
      }
    }
  }
  console.log(data);
});
