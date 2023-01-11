#!/usr/bin/python3

"""
module: mylist
"""


class MyList(list):
    """
    prints a sorted list
    """
    def print_sorted(self):
        """
        printing the sorted list
        """
        print(sorted(self))
        