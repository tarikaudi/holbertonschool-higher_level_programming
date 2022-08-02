#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
	const aux = this.height;
	this.height = this.width;
	this.width = aux;
  }

  double () {
   	this.height = this.height * 2;
	this.width = this.width * 2;
  }
};
