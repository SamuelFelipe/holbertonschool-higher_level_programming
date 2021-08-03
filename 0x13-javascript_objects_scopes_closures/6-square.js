#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      str += c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(str);
    }
  }
}

module.exports = Square;
