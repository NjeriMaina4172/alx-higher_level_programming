#!/usr/bin/python3
"""Readfile function"""


def read_file(filename=""):
    """ readfile - a functton that reads a file
    Args:
        @filename = the file name
    """

    with open(filename, encoding="utf-8") as myFile:
        read_data = myFile.read()
        print(read_data, end="")
        