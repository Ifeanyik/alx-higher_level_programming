#!/usr/bin/node
const args = process.argv;
let type = parseInt(args[2]);
if (!type) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < type; i++) {
    console.log('C is fun');
  }
}
