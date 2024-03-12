#!/usr/bin/node
/* an empty object */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w * h)) return;
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
