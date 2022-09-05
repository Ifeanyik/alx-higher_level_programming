#!/usr/bin/node
const args = process.argv;
const type = parseInt(args[2]);
if (!type) {
  console.log('Missing size');
} else {
  let i;
  let j;
  for (i = 0; i < type; i++) {
    let sqSide = '';
    for (j = 0; j < type; j++) {
      sqSide += 'X';
    }
    console.log(sqSide);
  }
}
