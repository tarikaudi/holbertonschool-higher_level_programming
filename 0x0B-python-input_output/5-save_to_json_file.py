#!/usr/bin/python3
"""comments are iḿportants"""


import json


def save_to_json_file(my_obj, filename):
    """write overrite"""
    with open(filename, 'w', encoding="UTF8") as data:
        json.dump(my_obj, data)
