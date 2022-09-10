#!/usr/bin/node
let count = 0;
exports.count = count;
exports.logMe = function (item) {
  if (!count && (count !== 0)) {
    count = 0;
    console.log(`${count}: ${item}`);
  } else {
    console.log(`${count}: ${item}`);
    count++;
  }
};
