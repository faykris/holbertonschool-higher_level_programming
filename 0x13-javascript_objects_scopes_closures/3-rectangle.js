#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0 || !w || !h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let str = '';
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        str += 'X';
      }
      console.log(str);
      str = '';
    }
  }
}

module.exports = Rectangle;
