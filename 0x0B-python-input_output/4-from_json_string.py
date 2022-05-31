#!/usr/bin/python3
"""containing modules of comments"""


import json


def from_json_string(my_str):
    """json open read """
    d = json.loads(my_str)
    return d
