#!/usr/bin/python3


def uppercase(inp):
    for c in inp:
        if c >= 'a' and c <= 'z':
            num = ord(c) - 32
        else:
            num = ord(c)
        print("{:c}".format(num), end='')
    print('')
