#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], (rerr, response, body) => {
  if (rerr) return console.log(rerr);
  fs.writeFile(process.argv[3], body, 'utf-8', function (werr) {
    if (werr) return console.log(werr);
  });
});
