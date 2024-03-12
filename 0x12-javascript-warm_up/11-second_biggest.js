#!/usr/bin/node
/* compare two argument */

function argument (argv) {
  let swap;
  if (argv.length <= 2) {
    console.log('0');
  } else {
    for (let i = 1; i < argv.length; i++) {
      for (let j = i; j > 0 && parseInt(argv[j]) < parseInt(argv[j - 1]); j--) {
        swap = argv[j];
        argv[j] = argv[j - 1];
        argv[j - 1] = swap;
      }
    }
    console.log(argv.length - 2);
  }
}

argument(process.argv.slice(2));
