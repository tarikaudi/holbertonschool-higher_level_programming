#!/usr/bin/python3
def no_c(my_string):
    aux = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            aux += i
    return (aux)
