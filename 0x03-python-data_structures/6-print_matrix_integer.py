#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        le = len(i)
        for j in i:
            le = le - 1
            print("{:d}".format(j), end="")
            if le:
                print(" ", end="")
        print("")
