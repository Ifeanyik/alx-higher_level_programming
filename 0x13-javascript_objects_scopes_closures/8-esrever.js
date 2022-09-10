#!/usr/bin/node

exports.esrever = function (list) {
  let listLength = 0;
  for (; list[listLength]; listLength++);
  const myList = [];
  listLength--;
  for (; listLength >= 0; --listLength) {
    myList.push(list[listLength]);
  }
  return myList;
};
