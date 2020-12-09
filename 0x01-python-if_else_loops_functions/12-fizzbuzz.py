#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        if not i % 3 and not i % 5:
            print("fizzbuzz", end=" ")
        elif not i % 3:
            print("fizz", end=" ")
        elif not i % 5:
            print("buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
