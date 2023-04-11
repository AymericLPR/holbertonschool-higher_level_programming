#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
    }
  }

  print () {
    let line = '';
    for (let printj = 0; printj < this.width; printj++) {
      line = line + 'X';
    }
    for (let printi = 0; printi < this.height; printi++) {
      console.log(line);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
