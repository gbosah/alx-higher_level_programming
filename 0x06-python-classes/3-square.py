#!/usr/bin/python3

"""Defines Class Square"""

class Square:
    """
    Simple class Square
    """

    def __init__(self, size=None):
        """
        class initializer
        """

        self.__size = size

        try:
            if self.__size < 0:
                raise ValueError("size must be >= 0")

            elif type(size) != int:
               raise TypeError("size must be an integer")

        except (ValueError, TypeError) as e:
            print(e)

    def area(self):
        """
        method for calculating area of 
        a square
        """

        return self.__size ** 2
