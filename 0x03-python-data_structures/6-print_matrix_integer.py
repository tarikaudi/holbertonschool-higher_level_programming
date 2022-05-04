#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for colum in matrix:
        largo = len(colum)
        cont = 0
        for fila in colum:
            print(f"{fila:d}", end='')
            if cont < (largo - 1):
                print(' ', end='')
            cont += 1
        print("")
