#!/usr/bin/python3
"""parses random strings"""


def text_indentation(text):
    """searches for what to find"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in range(len(text)):
        if text[c] in ":.?":
            print(text[c])
            print("")
        else:
            print(text[c], end="")
