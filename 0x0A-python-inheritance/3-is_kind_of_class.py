#!/usr/bin/python3
"""module to function ex 3"""


def is_kind_of_class(obj, a_class):
    """function return true or false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
