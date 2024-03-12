#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w * h)) return;
    this.width = w;
    this.height = h;
  }

  print () {
    let { width, height } = this;
    let row = '';
    for (; width > 0; width--) row += 'X';
    for (;height > 0; height--) console.log(row);
  }

  rotate () {
    const h = this.height;
    this.height = this.width;
    this.width = h;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
