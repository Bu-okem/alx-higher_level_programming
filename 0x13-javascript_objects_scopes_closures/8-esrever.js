#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  while (list.length > 0) {
    reversedList.push(list.pop());
  }
  return reversedList;
};
