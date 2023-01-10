#!/usr/bin/python3

"""
inherited class from Base
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class initializer """
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height
        

        self.integer_validator("width", width)
        self.integer_validator("height", height)
