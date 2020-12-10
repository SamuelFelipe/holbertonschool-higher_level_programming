#!/usr/bin/python3
import sys

add = 0

for i in sys.argv[1:]:
    add += int(i)
print("{}".format(add))
