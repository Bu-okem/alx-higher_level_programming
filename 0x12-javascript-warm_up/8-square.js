#!/usr/bin/node
const size = process.argv[2];
let n = 0;

if (!isNaN(size)) {
    while (n < size) {
        console.log('X'.repeat(size));
        n++;
    }
} else {
    console.log('Missing size');
}
