#!/usr/bin/python3
"""rectangle module
inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle
    Private instance attributes:
        - width
        - height 
    inherts from BaseGeometry
    """

    def __init__(self, width, height):
        """initiation method

        Arg:
            - width: rectangle width
            - height: rectangle height
        """
           
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
