#!/usr/bin/python3
"""module to start to use JSON"""
import json


def load_from_json_file(filename):
    '''write a string in json mode into a file'''
    with open(filename, "r") as f:
        return json.loads(f.read())
