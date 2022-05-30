#!/usr/bin/python3
"""module module"""


Rectangle = __import__('9-rectangle').Rectangle
"""import func"""


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """comments for the checker"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of"""
        return (self.__size ** 2)

    def __str__(self):
        """return a string"""
        return (f"[{self.__class__.__name__}] {self.__size}/{self.__size}")
