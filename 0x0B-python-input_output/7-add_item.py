#!/usr/bin/python3
"""Module"""


import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'
ml = []
try:
    ml = load_from_json_file(filename)
except FileNotFoundError:
    ml = []
for i in range(1, len(sys.argv)):
    ml.append(sys.argv[i])

save_to_json_file(ml, filename)
