#!/usr/bin/python3
"""
to_json_string module
"""
from json import dumps


def to_json_string(my_obj):
    """
    to_json_string - function returns JSON representation of an object (string)

    Args:
        my_obj: is the object

    Returns: the JSON representation of an object (string)
    """
    return dumps(my_obj)
