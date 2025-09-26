#!/usr/bin/node
const { argv } = require('node:process');

const first = argv[2];
const numFirst = parseInt(first, 10);

if (!isNaN(numFirst)) {
  const output = 'My number: ' + numFirst;
  console.log(output);
} else {
  console.log('Not a number');
}
