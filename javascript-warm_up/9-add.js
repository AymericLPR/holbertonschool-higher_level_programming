#!/usr/bin/node
const process = require('process');

const argv = process.argv;
const num1 = Number(argv[2]);
const num2 = Number(argv[3]);

console.log(num1 + num2);
