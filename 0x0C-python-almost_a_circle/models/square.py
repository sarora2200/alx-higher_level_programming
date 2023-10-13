#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """intialization method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method"""
        r = "[{}] ({})".format(self.__class__.__name__, self.id)
        c = "{}/{} - {}".format(self.x, self.y, self.width)
        return r + c
