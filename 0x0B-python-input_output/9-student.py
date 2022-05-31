#!/usr/bin/python3
"""module func for the"""


class Student():
    """class student"""

    def __init__(self, first_name, last_name, age):
        """age first last name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return json"""
        return self.__dict__
