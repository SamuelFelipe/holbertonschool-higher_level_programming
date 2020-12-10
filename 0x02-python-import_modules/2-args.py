#!/usr/bin/python3
import sys

ac = len(sys.argv) - 1
count = 1

if ac:
    print("{} arguments:".format(ac))
else:
    print("{} arguments.".format(ac))

for i in sys.argv[1:]:
    print("{}: {}".format(count, i))
    count += 1
