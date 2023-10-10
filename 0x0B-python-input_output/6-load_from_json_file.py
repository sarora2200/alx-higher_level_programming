#!/usr/bin/python3
"""
load_from_json_file module
"""
from json import loads


def load_from_json_file(filename):
    """
    load_from_json_file - function creates an Object from a “JSON file”

    Args:
        filename: the file name
    """
    with open(filename, 'r') as f:
        return loads(f.read())
