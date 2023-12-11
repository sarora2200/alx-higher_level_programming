#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const o = Number(process.argv[2]);
  for (let i = 0; i < o; i++) {
    let e = '';
    for (let j = 0; j < o; j++) {
      e += 'X';
    }
    console.log(e);
  }
}
