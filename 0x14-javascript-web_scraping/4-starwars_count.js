#!/usr/bin/node

const request = require('request');
let num = 0;

request(process.argv[2], (error, response, body) => {
  if (error) return console.log(error);
  for (const res of JSON.parse(body).results) {
    for (const chr of res.characters) {
      if (chr.search('18') > 0) num++;
    }
  }
  console.log(num);
});
