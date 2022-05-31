#!/usr/bin/python3
"""load modules func"""


import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


add = "add_item.json"

try:
    loaded = load_from_json_file(fname)
except FileNotFoundError:
    loaded = []

save_to_json_file(loaded + argv[1:], add)
