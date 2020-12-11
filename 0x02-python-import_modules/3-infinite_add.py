#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    add = 0

    for i in sys.argv[1:]:
           add += int(i)
    print("{}".format(add))
