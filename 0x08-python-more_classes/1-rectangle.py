#!/usr/bin/python3
"""Class defines a rectangle"""


class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    """Return property value"""
    def width(self):
        return self.__width

    @width.setter
    """Setter property"""
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    """Return property value"""
    def height(self):
        return self.__height

    @height.setter
    """Setter property"""
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
