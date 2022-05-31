#!/usr/bin/python3
"""comments needed forr"""


def read_file(filename=""):
    """reads // print"""
    with open(filename, 'r', encoding="UTF8") as f:
        for data in f:
            print(data, end="")
