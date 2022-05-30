#!/usr/bin/python3
"""odule to func dor the checker"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""imported func"""


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """comment dor the checker accept"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
