#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write_file: function that writes a string to a text file

    Args:
        filename: the file name.
        text: the text

    Returns: the number of characters written.
    """
    with open(filename, 'w', encoding="UTF-8") as f:
            return(f.write(text))
