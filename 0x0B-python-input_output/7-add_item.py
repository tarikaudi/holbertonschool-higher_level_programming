#!/usr/bin/python3
"""load modules func"""


import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


fname = "add_item.json"

try:
    load = load_from_json_file(fname)
except FileNotFoundError:
    load = []

save_to_json_file(load + argv[1:], fname)
