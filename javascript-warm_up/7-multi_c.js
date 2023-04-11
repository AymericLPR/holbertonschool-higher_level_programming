#!/usr/bin/node
const process = require('process');

const argv = process.argv;
const c = 'C is fun';
let i = 0;
const max = Number(argv[2]);

if (!max) {
  console.log('Missing number of occurrences');
} else {
  while (i < max) {
    console.log(c);
    i++;
  }
}
