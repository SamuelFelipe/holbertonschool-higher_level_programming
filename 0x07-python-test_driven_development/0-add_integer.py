#!/usr/bin/python3


"""
Returns the addition of two numbers

Function example:

    >>>add_integer(10, 11)
    21
"""


def add_integer(a, b=98):
    """
    Arguments:
        a: The first argument passed to the function
        b: The second argument passed to the function
    Raises:
        TypeError: if a not int or float value is passed to the function
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
