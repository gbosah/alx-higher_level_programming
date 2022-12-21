#!/usr/bin/python3

class Square:
    """
    Simple class Square
    """

    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if type(self.__size) != int:
                raise TypeError("size must be an integer")
            elif self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        except (TypeError, ValueError) as e:
            print(e)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if type(self.__position) != tuple:
                if self.__position[0] < 0 and self.__position[1] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
        except TypeError as e:
            print(e)

    def area(self):
        return self.__size ** 2

    def my_print(self):
        try:
            if type(self.__size) == str:
                raise TypeError("size must be integer")
            elif self.__size < 0:
                #print()
                raise ValueError("size must be >= 0")
            for i in range(self.__size):
                print("#" * self.__size)
        except TypeError as e:
            print(e)
