#!/usr/bin/python3
"""module to start to use JSON"""
import json


def save_to_json_file(my_obj, filename):
    '''write a string in json mode into a file'''
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
