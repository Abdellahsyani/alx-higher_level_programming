#!/usr/bin/python3
"""Module to add your arguments into JSON file."""
import sys
import json


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


item_list = []
try:
    item_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    f = open("add_item.json", 'w')
    f.close()
except json.decoder.JSONDecodeError:
    pass

item_list += sys.argv[1:]
save_to_json_file(item_list, "add_item.json")
