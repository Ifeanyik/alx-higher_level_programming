#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let h;
    let w;
    for (h = 0; h < this.width; h++) {
      let squareString = '';
      for (w = 0; w < this.width; w++) {
        squareString += c;
      }
      console.log(squareString);
    }
  }
}

module.exports = Square;
