#!/usr/bin/node

let fir = 0;
let sec = 0;
let i = 2;

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  while (process.argv[i]) {
    if (parseInt(process.argv[i]) > fir) {
      fir = parseInt(process.argv[i]);
    }
    i++;
  }
  i = 2;

  while (process.argv[i]) {
    if (parseInt(process.argv[i]) > sec && parseInt(process.argv[i]) !== fir) {
      sec = parseInt(process.argv[i]);
    }
    i++;
  }
  console.log(sec);
}
