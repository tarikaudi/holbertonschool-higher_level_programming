#!/usr/bin/python3
"""
function to divide a whole matrix 
"""


def matrix_divided(matrix, div):
    """This divide matrix by div"""

    if type(matrix) is not list or matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        for i in row:
            if type(i) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    """check if it is same size"""

    iterate = iter(matrix)
    lenght = len(next(iterated_matrix))
    if not all(len(j) == lenght for j in iterate):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(
        map(lambda x: list(map(lambda y: round((y / div), 2), x)), matrix)
    )
