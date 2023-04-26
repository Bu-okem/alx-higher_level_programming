#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const newString = process.argv[3];

fs.writeFile(file, newString, 'utf-8', function (err) {
  if (err) console.log(err);
});
