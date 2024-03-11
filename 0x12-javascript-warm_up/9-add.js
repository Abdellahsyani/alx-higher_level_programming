#!/usr/bin/node
/* addition two number */

function add (argv, a, b) {
  a = parseFloat(argv[2]);
  b = parseFloat(argv[3]);
  if (isNaN(a) || isNaN(b)) {
    console.log('NAN');
  } else {
    const sum = a + b;
    console.log(sum);
  }
}
add(process.argv);
