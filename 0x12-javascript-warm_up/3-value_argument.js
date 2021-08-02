#!/usr/bin/node

let i = 0;

while (process.argv[i]) {
  if (i === 2) {
    console.log(process.argv[2]);
  }
  i++;
}
if (i === 2) {
  console.log('No argument');
}
