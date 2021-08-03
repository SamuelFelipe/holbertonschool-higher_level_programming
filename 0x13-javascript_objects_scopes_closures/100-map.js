#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list);

const arr = list.map((val, indx) => val * indx);

console.log(arr);
