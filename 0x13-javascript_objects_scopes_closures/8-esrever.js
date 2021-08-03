#!/usr/bin/node

exports.esrever = function (list) {
  const array = [];
  for (let i = list.length; i; i--) {
    array.push(list[i - 1]);
  }
  return array;
};
