#!/usr/bin/python3

'''Class BaseGeometry'''


class BaseGeometry:
    '''Useless class'''

    def area(self):
        '''not implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validate the value'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
