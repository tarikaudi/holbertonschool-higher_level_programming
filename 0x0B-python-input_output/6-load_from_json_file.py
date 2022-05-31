#!/usr/bin/python3
"""comments are iḿportants"""


import json


def load_from_json_file(my_obj, filename):
    """write overrite"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
