#!/usr/bin/python3
"""module: class to json"""


def class_to_json(obj):
    """ class_to_json - a function that converts a class to json
    Args:
        @obj: the class
    """
    return obj.__dict__
    