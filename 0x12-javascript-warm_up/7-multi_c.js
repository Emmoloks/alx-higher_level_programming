#!/usr/bin/node
const arg = Math.floor(Number(process.argv[2]));
if (isNaN(arg)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
