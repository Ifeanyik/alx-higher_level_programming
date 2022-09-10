#!/usr/bin/node
const args = process.argv;
function factorial (number) {
  if (number !== 0) {
    return (number * factorial(number - 1));
  } else {
    return (1);
  }
}
if (!args[2]) {
  console.log('1');
} else {
  const arg = parseInt(args[2]);
  if (!arg && arg !== 0) {
    console.log('NaN');
  } else if (arg === 1) {
    console.log(1);
  } else if (arg === 0) {
    console.log(1);
  } else {
    const fact = factorial(arg);
    console.log(fact);
  }
}
