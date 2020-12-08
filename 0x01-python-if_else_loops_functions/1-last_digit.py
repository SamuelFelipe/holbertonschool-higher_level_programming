#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
if number >= 0:
    c = number % 10 
else:
   c = -number % 10
   c *= -1
if c > 5:
    string = "and is greater than 5"
elif c == 0:
    string = "and is 0" 
else:
    string = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {}".format(number, c, string))
