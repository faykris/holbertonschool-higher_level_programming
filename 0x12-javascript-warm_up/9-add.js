#!/usr/bin/node

function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);

  if (isNaN(num1) || isNaN(num2)) {
    return NaN;
  }

  return num1 + num2;
}

console.log(add(process.argv[2], process.argv[3]));
