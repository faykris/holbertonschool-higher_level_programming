#!/usr/bin/node

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

const number = parseInt(process.argv[2]);
let fact = 1;

if (isNaN(process.argv[2]) || number === 0) {
  console.log(fact);
} else if (number > 0) {
  fact = factorial(number);
  console.log(fact);
}
