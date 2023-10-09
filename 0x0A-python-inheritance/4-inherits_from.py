#!/usr/bin/python3
"""inherits_from module
finds if object is an instance of a class
"""


def inherits_from(obj, a_class):
    """function that returns True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.

   Arg:
        obj: is the object
        a_class: is the class to verify is an instance of

    Returns:True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
