#!/usr/bin/python3
""" module: write function"""


def append_write(filename="", text=""):
    """ write file-  a function that writes text in a file
    Args:
        @filename: the name of the file
        @text: the text to be written
    """

    count = 0
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
        