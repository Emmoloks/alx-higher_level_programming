#!/usr/bin/node
const myNum = Math.floor(Number(process.argv[2]));
if (!isNaN(myNum)) {
  console.log(`My number: ${myNum}`);
} else {
  console.log('Not a number');
}
