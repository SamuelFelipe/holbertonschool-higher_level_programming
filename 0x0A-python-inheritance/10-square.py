#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''Class Square that inherits from Rectangle'''


class Square(Rectangle):
    '''A Square'''

    def __init__(self, size):
        '''define a rectangle'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
