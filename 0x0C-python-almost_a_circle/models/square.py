#!/usr/bin/python3
'''class Square that inherits from Rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square, Rectangle child, do a square setting
    width and height with the same value'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize the class and inherits all the methods
        from the parent class Rectangle, set the width and height
        with te same value 'size'(required) and x, y still optional'''
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        '''Return a string with the square info
        [Square] (id) x/y - size'''
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    def update(self, *args, **kwargs):
        '''Update the square with *args or **kwargs.
        to args the input must be (id, size, x, y)'''
        argk = ('id', 'size', 'x', 'y')
        if args:
            for i in range(len(args)):
                exec('self.{} = args[{:d}]'.format(argk[i], i))
        if kwargs:
            for i in kwargs:
                exec('self.{} = kwargs[i]'.format(i))

    @property
    def size(self):
        '''Return the size value of the square'''
        return self.width

    @size.setter
    def size(self, size):
        '''Set the square size using the parent class verification'''
        self.width = size
        self.heigth = size
