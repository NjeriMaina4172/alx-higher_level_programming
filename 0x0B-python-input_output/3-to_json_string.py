#!/usr/bin/python3
"""module: to json string"""
import json


def to_json_string(myobj):
    """ to_json_string - a function that returns the json representation
    of an object string
    Args:
        @myobj: the object to convert to json
    """
    return json.dumps(myobj)
    