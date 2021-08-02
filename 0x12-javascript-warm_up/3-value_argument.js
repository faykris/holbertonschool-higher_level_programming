#!/usr/bin/node
import { argv } from 'process';

let i = 0;

argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  i = index;
});

if (i <= 1) {
  console.log('No argument');
}
