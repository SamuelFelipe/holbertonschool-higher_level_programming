#!/usr/bin/python3

'''Returns a boolean depending on \
whether the input values are equal'''


def inherits_from(obj, a_class):
    '''return true or false whether if the object
    is an instance than the class or not'''
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
