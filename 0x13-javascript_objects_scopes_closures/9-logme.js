#!/usr/bin/node

let n = 0;
exports.logMe = function (item) {
  console.log(`${n}: ${item}`);
  n++;
};
