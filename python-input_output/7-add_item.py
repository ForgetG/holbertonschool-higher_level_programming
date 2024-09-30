#!/usr/bin/python3
'''
Module 7-add_item

Script that adds all arguments to a Python list, and then save them to a file
'''
import json
import sys
import os

module_save = __import__('5-save_to_json_file')
module_load = __import__('6-load_from_json_file')

save_to_json_file = module_save.save_to_json_file
load_from_json_file = module_load.load_from_json_file

filename = 'add_item.json'
if not os.path.exists(filename):
    save_to_json_file([], filename)
items = load_from_json_file(filename)
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
