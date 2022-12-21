#!/usr/bin/python3

""" Defines a square """


class Square:
    """
    Simple class Square
    """

    def __init__(self, size=0):
        """
        class initializer
        """

        self.__size = size
        try:
            if int(size) < 0:
                raise ValueError("size must be >= 0")
            if type(self.__size) != int:
                raise TypeError("size must be an integer")
        except (ValueError, TypeError) as e:
            print(e)
