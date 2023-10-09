#!/usr/bin/python3
"""is_kind_of_class module
finds if object is an instance of class"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Arg:
        obj: is an object
        a_class: is a class to verify the instance of


    Returns:True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """

    return isinstance(obj, a_class)
