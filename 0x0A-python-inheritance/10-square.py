#!/usr/bin/python3

"""
inherited class
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ class initializer """
    def __init__(self, size) -> None:
        self.__size = size

        self.integer_validator("size", size)

    """ string printer """
    def __repr__(self) -> str:
        return f"[Rectangle] {self.__size}/{self.__size}"

    """ area calculator """
    def area(self):
        return self.__size * self.__size
