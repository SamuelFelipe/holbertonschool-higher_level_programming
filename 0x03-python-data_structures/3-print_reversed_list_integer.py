#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    le = len(my_list)
    if le:
        for i in reversed(my_list):
            print("{}".format(i))
