#!/usr/bin/python3
'''Class Square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A Square'''

    def __init__(self, size):
        '''define a rectangle'''
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self) -> str:
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
