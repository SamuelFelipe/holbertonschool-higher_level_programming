#!/usr/bin/python3

'''Print the data of a file'''


def read_file(filename=""):
    '''print the content of a file'''

    with open(filename, "r", encoding="utf-8") as f:
        print("{}".format(f.read()), end='')
