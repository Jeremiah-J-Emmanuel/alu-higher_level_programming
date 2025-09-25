#!/usr/bin/node
const {argv} = require("node:process")

first = argv[2]
second = argv[3]
concat = first + " is " + second
console.log(concat)
