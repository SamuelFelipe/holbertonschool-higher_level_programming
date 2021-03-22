#!/usr/bin/node

function factorial (a) {
  if (a > 1) {
    return a * factorial(a - 1);
  } else {
    return a;
  }
}

console.log(factorial(parseInt(process.argv[2])));
