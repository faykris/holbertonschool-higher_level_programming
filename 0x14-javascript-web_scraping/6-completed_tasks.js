#!/usr/bin/node

const request = require('request');
const todos = {};

request(process.argv[2], (err, response, body) => {
  if (err) return console.log(err);
  for (const todo of JSON.parse(body)) {
    if (todo.completed === true) {
      if (todos[todo.userId] === undefined) {
        todos[todo.userId] = 0;
      }
      todos[todo.userId] += 1;
    }
  }
  console.log(todos);
});
