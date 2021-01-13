#!/usr/bin/python3


class Rectangle:

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def __str__(self) -> str:
        rect = ''
        for i in range(0, self.area()):
            rect += '#'
            if i + 1 != self.area() and not (i + 1) % self.width:
                rect += '\n'
        return rect

    def __repr__(self) -> str:
        return '{self.__class__.__name__}({self.width}, {self.height})'.format(self=self)

    def __del__(self):
        print('Bye rectangle...')

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
