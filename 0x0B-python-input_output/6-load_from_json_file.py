#!/usr/bin/python3
"""comments are iḿportants"""


import json


def load_from_json_file(filename):
    """write overrite"""
    with open(filename, 'r') as f:
        return json.loads(f.read())
