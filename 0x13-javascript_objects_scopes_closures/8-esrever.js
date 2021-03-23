#!/usr/bin/node

exports.esrever = function (list) {
  const l = list.length - 1;
  const reverse = [];
  for (let i = 0; i <= l; i++) reverse.push(list[l - i]);
  return reverse;
};
