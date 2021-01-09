#!/usr/bin/python3


'''
Print a square

Usage example:
    >>>print_square(3)
    ###
    ###
    ###
'''


def print_square(size):
    '''
    raise a TypeError when size is not an integer and
    raise a ValueError when size in less than zero

    Example:
    >>>print_square("i love bugs")
    TypeError: size must be an integer
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size**2):
        print("#", end="")
        if i and not (i + 1) % size:
            print("")
    if size == 1:
        print("")
