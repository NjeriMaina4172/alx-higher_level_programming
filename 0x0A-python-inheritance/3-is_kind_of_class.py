#!/usr/bin/python3

"""
module: is kind of a class function
used to check if is instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    return true if isinstance else false
    """
    if isinstance(obj, a_class):
        return True
    return False
    