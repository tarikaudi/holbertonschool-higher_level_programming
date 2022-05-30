#!/usr/bin/python3
"""this module module func"""


class BaseGeometry():
    """class of base geometry"""

    def area(self):
        """comment for the checker"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
