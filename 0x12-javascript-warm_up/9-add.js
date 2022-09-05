#!/usr/bin/node
const args = process.argv;
function add(a, b) {
  console.log(a + b);
}
if (!args[2] || !args[3]) {
  console.log('NaN');
}
else {
  let var1 = parseInt(args[2]);
  let var2 = parseInt(args[3]);
  if (!var1 || !var2) {
    console.log('NaN');
  } else {
    add(var1, var2);
  }
}
