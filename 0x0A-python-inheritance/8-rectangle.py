#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''Class Rectangle that inherits from BaseGeometry'''


class Rectangle(BaseGeometry):
    '''A rectangle'''

    def __init__(self, width, height):
        '''define a rectangle'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
