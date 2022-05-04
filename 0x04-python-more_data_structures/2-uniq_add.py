#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    uniq = set(my_list)

    for num in uniq:
        res += num
    return(res)
