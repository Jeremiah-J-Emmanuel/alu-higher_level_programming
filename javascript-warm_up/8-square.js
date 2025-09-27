#!/usr/bin/node

const { argv } = require('node:process');
const convNum = parseInt(argv[2]);

if (!isNaN(convNum)) {
  let i = 0;
  const rows = 'X'.repeat(convNum);
  while (i < convNum) {
    console.log(rows);
    i++;
  }
} else {
  console.log('Missing size');
}
