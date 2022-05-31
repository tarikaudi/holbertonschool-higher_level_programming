#!/usr/bin/python3
"""modules func func comments"""


def pascal_triangle(n):
    var = []
    """def pascal_triangle"""
    for i in range(n):
        row = []
        if i is 0:
            row.append(1)
            var = var + row
        else:
            for a in range(i):
                row
