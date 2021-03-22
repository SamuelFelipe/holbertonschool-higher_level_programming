#!/usr/bin/node

const a = parseInt(process.argv[2]);
if (!a) {
  console.log('Missing size');
} else {
  let str = '';

  for (let i = 0; i < a; i++) {
    str = str + 'X';
  }
  for (let i = 0; i < a; i++) {
    console.log(str);
  }
}
