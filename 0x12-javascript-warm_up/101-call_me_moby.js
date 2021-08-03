#!/usr/bin/node
let callMeMoby = function () {};
callMeMoby = function (x, theFunction) {
  let i = 0;

  while (i < x) {
    theFunction();
    i++;
  }
};
exports.callMeMoby = callMeMoby;
