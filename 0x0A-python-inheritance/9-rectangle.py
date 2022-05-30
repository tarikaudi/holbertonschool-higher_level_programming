#!/usr/bin/python3
"""ocmmentsfor the cheker"""


class BaseGeometry:
    """class"""

    def area(self):
        """comment for the checker"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry)
    """class"""
    def __init__(self, width, height):
        """comment dor the checker accept"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return the area"""
        return self.__height * self.__width

    def __str__(self):
        """return a string"""
        return (f"[{type(self).__name__}] {self.__width}/{self.__height}")
