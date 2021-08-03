#!/usr/bin/node
let addMeMaybe = function () {};
addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
exports.addMeMaybe = addMeMaybe;
