#!/usr/bin/node

const request = require('request');

const idFilm = process.argv[2];

const API = 'https://swapi-api.hbtn.io/api/films/' + idFilm;

request(API, function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
  }
  const objFilm = JSON.parse(body);
  objFilm.characters.forEach(element => {
    request(element, function (error, response, body) {
      if (error != null) {
        console.error('error:', error);      }
      const objActor = JSON.parse(body);
      console.log(objActor.name);
    });
  });
});
