#!/usr/bin/node
 const {argv} = require("node:process")

 const number = argv[2]
 const num = parseFloat(number)
 if (!isNaN(num)) {
    let i = 0
    while (i < num) {
        console.log("C is fun")
        i++} 
    }else{
        console.log("Missing number of occurences")
    }
