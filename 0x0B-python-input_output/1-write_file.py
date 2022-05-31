#!/usr/bin/python3
"""comments are important"""


def write_file(filename="", text=""):
    """write or overwrite"""
    with open(filename, 'w', encoding="UTF8") as data:
        d = data.write(text)
    return d
