#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);
const map1 = list.map((x, y) => x * y);
console.log(map1);
