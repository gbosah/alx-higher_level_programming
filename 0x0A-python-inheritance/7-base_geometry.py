#!/usr/bin/python3

"""
Base Class
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""
    def area(self):
        """ raise Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checkers """
        if type(value) != int:
            raise TypeError(f" {name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
