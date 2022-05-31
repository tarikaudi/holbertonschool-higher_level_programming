#!/usr/bin/python3
"""module func for the"""


class Student():
    """class student"""

    def __init__(self, first_name, last_name, age):
        """age first last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return json"""
        if attrs is None:
            return self.__dict__
        else:
            new = {}
            for attribute in attrs:
                if attribute in self.__dict__.keys():
                    new[attribute] = self.__dict__[attribute]
            return new
