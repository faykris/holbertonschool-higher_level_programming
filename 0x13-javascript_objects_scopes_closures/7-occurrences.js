#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let nbo = 0;

  while (i < list.length) {
    if (list[i] === searchElement) {
      nbo++;
    }
    i++;
  }
  return nbo;
};
