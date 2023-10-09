#!/usr/bin/python3
"""module is_same_class
returns True if the object is exactly an instance of the specified class ;
otherwise False"""


def is_same_class(obj, a_class):
    """Function to determine if obj is an instance of a_class

    Args:
        - obj: object to look at
        - a_class: class to verify the instanceof

        Returns: True if obj is an instance of a_class
    False otherwise
    """

    return type(obj) is a_class
