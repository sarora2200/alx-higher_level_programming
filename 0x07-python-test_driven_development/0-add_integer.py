#!/usr/bin/python3
"""defines an integer addition function."""


def add_integer(a, b=98):

    """Returns an integer: the addition of a and b.

    a and b must be first casted to integers if they are float

    Raises:
        TypeError: if a or b is a non-integer or non_float.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":

    import doctest

    doctest.testfile("tests/0-add_integer.txt")
