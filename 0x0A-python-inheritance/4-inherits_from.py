#!/usr/bin/python3
"""
function that returns true if the object is an instance of the class
that inherited form the specified class
"""


def inherits_from(obj, a_class):
    """
    returns true if object is an instance of a class
    else false
    """
    return type(obj) != a_class and isinstance(obj, a_class)
    