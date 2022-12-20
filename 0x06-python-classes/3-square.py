#!/usr/bin/python3
"""creating the Square class"""


class Square():
    """creating the init function"""
    def __init__(self, size=0):
        """ initializing the variable size and setting it to a
        private attribute. Also checking for typeError and value errors
        Args:
            size(int): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2