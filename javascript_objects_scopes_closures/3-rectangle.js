#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let i = 1
    while (i <= this.height) {
        const str = "X";
        const repeatedStr = str.repeat(this.width);
        console.log(repeatedStr);
        i++;
    }
  }
}

module.exports = Rectangle;
