#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let n = 0;
    while (n < this.height) {
      console.log(c.repeat(this.width));
      n++;
    }
  }
}
module.exports = Square;
