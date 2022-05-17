#!/usr/bin/python3
"""yo cante no mas"""


class Square:
    """size size size"""

    def __init__(self, size=0):
        self.__size = size
        if (type(size) != int):
            raise TypeError("size must be a integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
