#!/usr/bin/python3


def print_last_digit(number):
    if number >= 0:
        c = number % 10
    else:
        c = -number % 10
    print("{:d}".format(c), end='')
    return c
