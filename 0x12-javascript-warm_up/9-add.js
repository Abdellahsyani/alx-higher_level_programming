#!/usr/bin/node
/* addition two number */

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NAN');
  } else {
    const sum = parseInt(a) + parseInt(b);
    console.log(sum);
  }
}
const [, , firstArg, secondArg] = process.argv;
add(firstArg, secondArg);
