#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
const x = Number(process.argv[2]);
let i = 0;
for (; i < x; i++) {
  console.log('C is fun');
}
