#!/usr/bin/python3
"""comments are important"""


def append_write(filename="", text=""):
    """write or overwrite"""
    with open(filename, 'w', encoding="UTF8") as data:
        d = data.write(text)
    return d
