#!/usr/bin/node
/* print a square */

function printS (argv) {
  let arr;
  if (argv[2]) {
    arr = parseFloat(argv[2]);
  }
  if (!isNaN(arr) && Number.isInteger(arr)) {
    for (let i = 0; i < arr; i++) {
      let row = '';
      for (let j = 0; j < arr; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
}
printS(process.argv);
