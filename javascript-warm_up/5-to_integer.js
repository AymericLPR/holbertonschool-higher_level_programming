#!/usr/bin/node
const process = require('process');

const argv = process.argv;
const check = Number(argv[2]);
if (!check) {
  console.log('Not a number');
} else {
  console.log('My number: ' + check);
}
