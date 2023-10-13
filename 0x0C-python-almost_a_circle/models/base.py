#!/usr/bin/python3
"""Modules for class base
It takes a private instance object
"""
import json
import os


class Base:
    """Declaring the base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Defining the class constructor
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string"""
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)
