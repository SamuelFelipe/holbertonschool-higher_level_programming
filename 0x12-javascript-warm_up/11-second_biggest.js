#!/usr/bin/node

let max = 0;
let lmax = 0;

if (process.argv.length <= 3) {
  console.log(max);
} else {
  max = parseInt(process.argv[2]);
  for (let i = 2; i < process.argv.length; i++) {
    if (max < parseInt(process.argv[i])) {
      lmax = max;
      max = parseInt(process.argv[i]);
    }
  }
  console.log(lmax);
}
