#!/usr/bin/node
/* prints two arguments */

function argument (argv) {
  console.log(process.argv[2], 'is', process.argv[3]);
}
argument(process.argv);
