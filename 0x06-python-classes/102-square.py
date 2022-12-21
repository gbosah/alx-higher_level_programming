#!/usr/bin/python3

"""Class Definition"""


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
            if size < 0:
                raise ValueError("size must be >= 0")
            elif not isinstance(size, int):
                raise TypeError("must be int")
        except (ValueError, TypeError) as e:
            print(e)

    @property
    def size(self):
        """
        size getter func
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter func
        """

        self.__size = value

    def __eq__(self, other):
        """
        checks if both instance are equal
        """

        return self.__size == other.__size

    def __lt__(self, other):
        """
        checks if one instance is less
        than the other
        """

        return self.__size < other.__size

    def __le__(self, other):
        """
        checks if one instance is less
        than or equal to the other
        """

        return self.__size <= other.__size

    def __ne__(self, other):
        """
        checks if one instance is not
        equal to the other
        """

        return self.__size != other.__size

    def __ge__(self, other):
        """
        checks if one instance is greater
        than or equal to the other
        """

        return self.__size >= other.__size

    def area(self):
        """"
        area calc func
        """

        try:
            if not isinstance(self.__size, int):
                raise TypeError("size must be integer")
            return self.__size ** 2
        except TypeError as e:
            print(e)
