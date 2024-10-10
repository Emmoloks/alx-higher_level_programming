#!/usr/bin/node
// printing if our node.js file runs with an argument
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
