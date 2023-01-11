#!/usr/bin/python3
"""module: class Student"""


class Student():
    """ initialize public variables"""
    first_name = None
    last_name = None
    age = 0

    def __init__(self, first_name, last_name, age):
        """ initializing the init function
        Args:
            @first_name: the first name of the student
            @last_name: the last name of the student
            @age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ To json - function to return a dictionary representation
        of a student
        Args:
            @attrs: the attribtes passed
        """

        if (type(attrs) == list and all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
        