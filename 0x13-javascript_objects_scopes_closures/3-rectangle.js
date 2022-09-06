#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
  }

  print() {
    let h;
    let j;
    for (h = 0; h < this.height; h++) {
      let shapeString = '';
      for (j = 0; j < this.width; j++) {
        shapeString += 'X';
      }
      console.log(shapeString);
    }
  }
}

module.exports = Rectangle;
