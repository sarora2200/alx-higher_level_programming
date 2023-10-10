#!/usr/bin/python3
"""
from_json_string
"""
from json import loads


def from_json_string(my_str):
    """
    from_json_string -  function returns an object represented by a JSON string

    Args:
        my_str: string

    Returns: an object represented by a JSON string
    """
    return loads(my_str)
