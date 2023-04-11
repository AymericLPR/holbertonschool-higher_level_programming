#!/usr/bin/node
const process = require('process');

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const argv = process.argv;
const number = Number(argv[2]);

if (!number) {
  console.log(1);
} else {
  console.log(factorial(number));
}
