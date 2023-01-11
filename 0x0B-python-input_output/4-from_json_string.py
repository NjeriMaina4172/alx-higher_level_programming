#!/usr/bin/python3
""" module:from json string"""
import json


def from_json_string(my_str):
    """ form_json_string - a function that converts json string to obj
    Args:
        @my_str: the json string
    """
    return json.loads(my_str)
    