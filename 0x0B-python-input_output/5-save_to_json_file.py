#!/usr/bin/python3
"""
save_to_json_file module
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - function writes an Object to a text file.

    Args:
        my_obj: object
        filename: the file name
    """
    with open(filename, 'w') as f:
        dump(my_obj, f)
