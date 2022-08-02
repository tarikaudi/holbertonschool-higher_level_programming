#!/usr/bin/node

exports.esrever = function (list) {
   const largo = list.length - 1;
   const copy = [];

   for (let i = largo; i >= 0; i--) {
	copy.push(list[i]);
   }
   return copy;
};
