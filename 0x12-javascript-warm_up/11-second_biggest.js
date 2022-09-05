#!/usr/bin/node
const args = process.argv;
if (!args[2]) {
  console.log(0);
} else if (args[2] && !args[3]) {
  console.log(0);
} else {
  let prevVar = 0;
  let largest = 0;
  let i;
  for (i = 2; args[i]; i++) {
    if (args[i] > largest) {
      prevVar = largest;
      largest = args[i];
    } if ((args[i] < largest) && args[i] > prevVar) {
      prevVar = args[i];
    }
  }
  console.log(prevVar);
}      
