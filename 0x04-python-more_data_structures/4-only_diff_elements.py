#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    suma = set_1.union(set_2)
    igual = set_1.intersection(set_2)
    diff = suma - igual
    return(diff)
