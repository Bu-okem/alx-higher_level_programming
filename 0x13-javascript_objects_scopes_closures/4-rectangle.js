#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let n = 0;
    while (n < this.height) {
      console.log('X'.repeat(this.width));
      n++;
    }
  }

  rotate () {
    const holder = this.width;
    this.width = this.height;
    this.height = holder;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
