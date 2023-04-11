#!/usr/bin/node
const process = require('process');

const argv = process.argv;
const character = 'X';
const size = Number(argv[2]);
let i = 0;
let j = 0;
let line = '';

if (!size) {
  console.log('Missing size');
} else {
  while (i < size) {
    line = line + character;
    i++;
  }

  while (j < size) {
    console.log(line);
    j++;
  }
}
