#!/usr/bin/node

const { argv } = require('node:process');
const a = argv[2];
const b = argv[3];
const num1 = parseInt(a);
const num2 = parseInt(b);

function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    const output = a + b;
    console.log(output);
  } else {
    console.log('NaN');
  }
}

add(num1, num2);
