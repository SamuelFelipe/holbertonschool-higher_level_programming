#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        l = len(i)
        for j in i:
            l  = l - 1
            print("{:d}".format(j), end="")
            if l:
                print(" ", end="")
        print("")
