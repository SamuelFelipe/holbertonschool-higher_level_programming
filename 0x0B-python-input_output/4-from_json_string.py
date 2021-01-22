#!/usr/bin/python3
"""module to start to use JSON"""
import json


def from_json_string(my_obj):
    '''return a string in json mode'''
    return json.loads(my_obj)

