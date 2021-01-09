#!/usr/bin/python3


'''
Print the arguments pased to the function

Usage example:
    >>>say_my_name("Bob", "Marley")
    My name is Bob Marley
'''


def say_my_name(first_name, last_name=""):
    '''
    Raise a error if any of the argument is a invalid one
    Example:

        >>>say_my_name(12, 22)
        TypeError: first_name must be a string
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
