#!/usr/bin/python3
from models.rectangle import Rectangle
'''class Square that inherits from Rectangle'''


class Square(Rectangle):
    '''Class Square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize'''
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        '''Return a string with the square info'''
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    def update(self, *args, **kwargs):
        '''Update the square'''
        argk = ('id', 'size', 'x', 'y')
        if args:
            for i in range(len(args)):
                exec('self.{} = args[{:d}]'.format(argk[i], i))
        if kwargs:
            for i in kwargs:
                exec('self.{} = kwargs[i]'.format(i))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.heigth = size
