#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filepath, data, 'utf8', (err) => {
  if (err) {
    console.error(`Error writing to file: ${err}`);
  }
});
