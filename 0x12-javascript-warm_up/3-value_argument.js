#!/usr/bin/node
/* print the first argument */

function argument (argv) {
  if (process.argv[2]) console.log(process.argv[2]);
  else console.log('No argument');
}
argument(process.argv);
