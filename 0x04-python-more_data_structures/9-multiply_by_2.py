#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new = {}
    mul2 = 0
    for n in a_dictionary:
        mul2 = a_dictionary[n] * 2
        new[n] = mul2
    return new
