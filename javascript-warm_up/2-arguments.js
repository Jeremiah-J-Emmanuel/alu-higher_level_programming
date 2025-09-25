#!/usr/bin/env node
const { argv } = require('node:process')

let len = argv.length

if len > 2{
    console.log("Arguments Found")
}else if len == 3{
    console.log("Argument found")
}else {
console.log("No argument")
}

