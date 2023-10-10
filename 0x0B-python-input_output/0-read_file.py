#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTP8) and prints it to stdout
    Args:
        filename: name of the file
    """
    with open(filename, 'r') as f:
        for i in f:
            print(i, end="")
    f.closed
