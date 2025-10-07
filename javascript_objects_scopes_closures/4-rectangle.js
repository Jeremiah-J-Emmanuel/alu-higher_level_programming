#!/usr/bin/node
#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 1;
    while (i <= this.height) {
      const str = 'X';
      const repeatedStr = str.repeat(this.width);
      console.log(repeatedStr);
      i++;
    }
  }

  rotate () {
    let i = 1;
    let h1 = this.height;
    let w1 = this.width;;

    this.height = w1;
    this.width = h1;

    while (i <= this.height) {
      const str = 'X';
      const repeatedStr = str.repeat(this.width);
      console.log(repeatedStr);
      i++;}
}

  double () {
    let i = 1;
    let h1 = this.height * 2;
    let w1 = this.width * 2;

    while (i <= h1) {
      const str = 'X';
      const repeatedStr = str.repeat(w1);
      console.log(repeatedStr);
      i++;
    }
}

module.exports = Rectangle;
