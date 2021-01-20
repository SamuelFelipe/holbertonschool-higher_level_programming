#!/usr/bin/python3

'''Returns a boolean depending on \
whether the input values are equal'''


def is_same_class(obj, a_class):
    '''return true or false whether if the object
    is exactly the same than the class or not'''
    return type(obj) == a_class
