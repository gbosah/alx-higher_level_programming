#!/usr/bin/python3

import math

"""Class Magic"""


class MagicClass:

    def __init__(self, radius):
        """
        Class initializer
        """
        
        self.__raduis = 0
        if type(radius) is not int and type(radius) is not float:
            self.__radius = radius


    def area(self):
        """
        area calc func
        """

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        circumference calc func
        """

        return 2 * math.pi * self.__radius
