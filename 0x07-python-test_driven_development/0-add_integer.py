#!/usr/bin/python3
"""
This is "0-add_integer" module
The module supplies one function, add_integer(a, b=98). For example,
>>> add_integer(1, 2)
3
"""

def add_integer(a, b=98):
    """
    Add integer function
    adds two integers together and returns the sum
    arg a: first integer
    arg b: second integer
    """
    if isinstance(a, str) or a is None:
        raise TypeError("a must be an integer")
    if isinstance(b, str) or b is None:
        raise TypeError("b must be an integer")


    a, b = int(a), int(b)

    return a + b
