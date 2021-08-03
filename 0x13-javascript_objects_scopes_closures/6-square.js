#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    let i = 0;
    let j = 0;
    let str = '';

    if (!c) {
      c = 'X';
    }

    for (i = 0; i < this.width; i++) {
      for (j = 0; j < this.width; j++) {
        str += c;
      }
      console.log(str);
      str = '';
    }
  }
}

module.exports = Square;
