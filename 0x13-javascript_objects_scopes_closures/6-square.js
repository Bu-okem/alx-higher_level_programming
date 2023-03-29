#!/uusr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const n = 0;
    while (n < this.height) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
