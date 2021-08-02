#!/usr/bin/node
import { argv } from 'process';

let i = 0;

argv.forEach((val, index) => {
  i = index;
});

if (i <= 1) {
  console.log('No argument');
} else if (i === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
