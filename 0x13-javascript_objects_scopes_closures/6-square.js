#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = 'C';
    let i = 0;
    let j = 0;
    let str = '';

    if (!c) {
      char = 'X';
    }

    for (i = 0; i < this.width; i++) {
      for (j = 0; j < this.width; j++) {
        str += char;
      }
      console.log(str);
      str = '';
    }
  }
}

module.exports = Square;
