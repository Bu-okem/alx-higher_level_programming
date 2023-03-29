#!/usr/bin/node

const len = process.argv.length - 2;
const list = process.argv.slice(2);

if (len <= 1) {
  console.log('0');
} else {
  list.sort((a, b) => {
    return a - b;
  });
  console.log(list[len - 2]);
}
