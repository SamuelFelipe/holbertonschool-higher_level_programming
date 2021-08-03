#!/usr/bin/node

let biggest = 0;

if (process.argv.length <= 3) {
  console.log(biggest);
} else {
  biggest = parseInt(process.argv[2]);
  let secondBiggest = parseInt(process.argv[3]);
  process.argv.forEach((value) => {
    if (parseInt(value) > biggest) {
      secondBiggest = biggest;
      biggest = parseInt(value);
    } else if (parseInt(value) > secondBiggest &&
               parseInt(value) < biggest) {
      secondBiggest = parseInt(value);
    }
  });

  console.log(secondBiggest);
}
