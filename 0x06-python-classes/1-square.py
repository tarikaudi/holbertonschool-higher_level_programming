#!/usr/bin/python3
"""comment of class"""


class Square:
    """square with private size"""
    __size = 0

    def __init__(self, size_square=None):
        if size_square is not None:
            self.__size = size_square
