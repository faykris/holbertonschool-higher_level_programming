#!/usr/bin/node

const number = parseInt(process.argv[2]);
let i = 0;

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else if (number > 0){
    while (i < number) {
      console.log('C is fun');
      i++;
    }
}
