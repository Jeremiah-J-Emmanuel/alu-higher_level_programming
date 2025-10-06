#!/usr/bin/node
// A script that reads and prints the content of a file

const fs = require('fs');

// Get file path from the first command line argument
const filePath = process.argv[2];

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
