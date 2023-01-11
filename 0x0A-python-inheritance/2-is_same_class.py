#!/usr/bin/python3

"""
a function that returns true if the object is exactly an instance
of the specified cladd
"""


def is_same_class(obj, a_class):
    """
    return true if instance else false
    """
    if type(obj) == a_class:
        return True
    return False
    