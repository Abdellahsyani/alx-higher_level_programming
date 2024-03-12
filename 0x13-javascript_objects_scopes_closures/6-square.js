#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c = 'X') {
    let { width, height } = this;
    let row = '';

    for (; width > 0; width--) row += c;
    for (;height > 0; height--) console.log(row);
  }
}

module.exports = Square;
