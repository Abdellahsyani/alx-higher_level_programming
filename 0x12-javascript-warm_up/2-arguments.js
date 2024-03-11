#!/usr/bin/node
/* print arguments */

function argument (argv) {
  if (argv.length <= 2) console.log('No argument');
  else if (argv.length === 3) console.log('Argument found');
  else console.log('Arguments found');
}
argument(process.argv);
