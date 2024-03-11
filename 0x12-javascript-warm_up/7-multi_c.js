#!/usr/bin/node
/* print x times using loop */

function Totimes (argv) {
  let varr;
  if (argv[2]) {
    varr = parseFloat(argv[2]);
  }

  if (!isNaN(varr) && Number.isInteger(varr)) {
    for (let i = 0; i < varr; i++) {
      console.log('C is fun');
    }
  }
}
Totimes(process.argv);
