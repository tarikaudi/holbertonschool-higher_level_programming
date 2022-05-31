#!/usr/bin/python3
"""modules func func comments"""


def pascal_triangle(n):
    """print triangle"""
    pascal_tri = []
    if n <= 0:
        return []
    for i in range(n):
        a = 11 ** i
        row = [int(digit) for digit in str(a)]
        pascal_tri += [row]
    return pascal_tri
