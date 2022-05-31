#!/usr/bin/python3
"""comments are iḿportants"""


import json


def load_from_json_file(my_obj, filename):
    """write overrite"""
    with open(filename, 'r', encoding="UTF8") as data:
        file_loaded = json.load(data)
    return file_loaded
