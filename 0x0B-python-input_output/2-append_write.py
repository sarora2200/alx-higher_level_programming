#!/usr/bin/python3
"""
append_write module
"""


def append_write(filename="", text=""):
    """
    append_write - function that appends a string at the end of a text file

    Args:
        filename: the file name
        text: the text

    Returns: the number of characters added.
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        return (f.write(text))
