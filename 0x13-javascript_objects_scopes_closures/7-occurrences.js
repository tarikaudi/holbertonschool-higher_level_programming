#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;

  list.forEach(elem => {
    if (elem === searchElement) { c++; }
  });
  return c;
};
