#!/usr/bin/node
const { argv } = require('node:process');

function factorial () {
  const number = parseInt(argv[2]);
  if (number === 0) {
    console.log(1);
  } else if (!isNaN(number)) {
    let output = number;
    let i = 2;
    while (i < number) {
      output = output * i;
      i++;
    }
    console.log(output);
  } else {
    console.log(1);
  }
}
