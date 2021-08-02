#!/usr/bin/node

const number = parseInt(process.argv[2]);
let i = 0;
let j = 0;
let hash = '';

if (isNaN(number)) {
  console.log('Missing size');
} else if (number > 0) {
  while (i < number) {
    while (j < number) {
      hash += 'X';
      j++;
    }
    console.log(hash);
    j = 0;
    hash = '';
    i++;
  }
}
