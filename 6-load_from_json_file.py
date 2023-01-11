#!/usr/bin/python3
"""module: load from json file"""
import json


def load_from_json_file(filename):
    """ load_from_json_file - a function that loads data from a json file
    Args:
        @filename: the name of the json file
    """

    with open(filename, encoding="utf-8") as file:
        json_data = file.read()
        return json.loads(json_data)
        