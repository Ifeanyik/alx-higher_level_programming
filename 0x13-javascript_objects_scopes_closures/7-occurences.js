#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  let i;
  for (i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      occurences += 1;
    }
  }
  return occurences;
};
