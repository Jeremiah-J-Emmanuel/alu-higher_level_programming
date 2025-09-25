#!/usr/bin/node
const { argv } = require("node:process")

const first = argv[2]
const numFirst = parseInt(first)

if (!isNaN(numFirst)) {
  const output = "My number: " + numFirst
  console.log(output)
} else {
  console.log("Not a number")
}

