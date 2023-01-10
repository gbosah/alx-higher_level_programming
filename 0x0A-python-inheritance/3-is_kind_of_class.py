#!/usr/bin/python3

"""
module for func is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """ returns True if obj is instance of class else False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
