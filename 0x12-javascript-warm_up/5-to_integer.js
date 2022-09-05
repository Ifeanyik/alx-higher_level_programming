#!/usr/bin/node
const args = process.argv;
if (!args[2]) {
  console.log('Not a number');
} else {
  const type = parseInt(args[2]);
  if (!type) {
    console.log('Not a number');
  } else {
    console.log('My number:', type);
  }
}
