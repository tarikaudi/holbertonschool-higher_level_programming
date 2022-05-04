#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def potencia(lista):
        res = list(map(lambda x: x ** 2, lista))
        return res
    ret = list(map(potencia, matrix))
    return ret
