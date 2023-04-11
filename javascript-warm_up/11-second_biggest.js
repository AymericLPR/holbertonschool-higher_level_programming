#!/usr/bin/node
const process = require('process');

const argv = process.argv;
let secondBiggest = 0;
let biggest = 0;
if (argv.length <= 3) {
  console.log(0);
} else {
  argv.slice(2, argv.length).forEach((num) => {
    if (Number(num) > biggest) {
      secondBiggest = biggest;
      biggest = Number(num);
    } else if (Number(num) > secondBiggest) {
      secondBiggest = Number(num);
    }
  });
  console.log(secondBiggest);
}
