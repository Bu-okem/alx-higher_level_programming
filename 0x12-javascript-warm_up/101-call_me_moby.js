#!/usr/bin/node

exports.callMeMoby = function (num, func) {
  let i = 0;
  for (i; i < num; i++) {
    func();
  }
};
