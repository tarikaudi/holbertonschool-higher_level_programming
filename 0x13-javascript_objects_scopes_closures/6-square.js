#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let a = 0; a < this.height; a++) {
      console.log(c.repeat(this.height));
    }
  }
};
