#!/usr/bin/python3
"""func func func in ypypy"""


def inherits_from(obj, a_class):
    """return true or falseee"""
    if issubclass(obj.__class__, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
