#!/usr/bin/python3
"""Module that adds all arguments to a python list and
saves to a json file
"""


import sys
import os


save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

argv_list = []
if os.path.exists("add_item.json"):
    argv_list = load_file("add_item.json")
for i in sys.argv:
    argv_list.append(i)
save_file(argv," add_item.json")
