#!/usr/bin/python3


class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.area()):
            if not i or not i % self.__size:
                for j in range(0, self.position[0]):
                    print(" ", end="")
            print("#", end="")
            if i and not (i + 1) % self.__size:
                print("")
        if self.__size == 0:
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif min(position) < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
