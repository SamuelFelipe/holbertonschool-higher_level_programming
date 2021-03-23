#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) c = 'X';
    let str = '';
    for (let i = 0; i < this.width; i++) {
      str += c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(str);
    }
  }
}

module.exports = Square;
