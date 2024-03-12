#!/usr/bin/node
/* factorial */

function Factorial (n) {
  if (isNaN(n)) return 1;
  else if (n === 0 || n === 1) return 1;
  else {
    return n * Factorial(n - 1);
  }
}

function calculateFactorial (argv) {
  const inputNumber = parseInt(argv[2]);
  if (isNaN(inputNumber)) {
    console.log('1');
  } else {
    const result = Factorial(inputNumber);
    console.log(result);
  }
}

calculateFactorial(process.argv);
