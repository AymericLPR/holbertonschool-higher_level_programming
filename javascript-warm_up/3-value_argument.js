#!/usr/bin/node
const process = require('process');

const argv = process.argv;
if (!argv[2]) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
