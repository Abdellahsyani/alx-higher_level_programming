#!/usr/bin/node
/* print a number */

function printNumber (argv) {
  let firstarg;
  if (argv[2]) firstarg = parseFloat(argv[2]);
  if (!isNaN(firstarg) && Number.isInteger(firstarg)) {
    console.log('My number:', firstarg);
  } else {
    console.log('Not a number');
  }
}
printNumber(process.argv);
