#!/usr/bin/python3

"""
module for dunc inherits_from
"""


def inherits_from(obj, a_class):
    """ returns True else False """
    if isinstance(obj, a_class):
        if type(obj) != a_class:
            return True
    else:
        return False
