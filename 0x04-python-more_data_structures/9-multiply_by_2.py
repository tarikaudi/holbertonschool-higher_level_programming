#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cop = a_dictionary.copy()
    for i in a_dictionary:
        cop[i] *= 2
    return cop
