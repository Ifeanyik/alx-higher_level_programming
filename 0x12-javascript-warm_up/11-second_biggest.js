#!/usr/bin/node
const args = process.argv;
if (!args[2]) {
  console.log(0);
} else if (args[2] && !args[3]) {
  console.log(0);
} else {
  let secondLargest = args[2];
  let largest = args[2];
  let i;
  for (i = 3; args[i]; i++) {
    if (i == 3) {
      if (args[i] > largest) {
        secondLargest = largest;
        largest = args[i];
      } else {
        if (args[i] != largest) {
          secondLargest = args[i];
        }
      }
    } else {
      if (args[i] > largest) {
        secondLargest = largest;
        largest = args[i];
      } else {
        if (!secondLargest) {
          secondLargest = args[i];
        }
        if ((args[i] < largest) && (args[i] > secondLargest)) {
          secondLargest = args[i];
        }
      }
    }
  }
  console.log(secondLargest);
}
