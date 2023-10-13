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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @classmethod
    def create(cls, **dictionary):
         """returns an instance with all attributes already set"""
         instance = cls(1, 1)
         instance.x = 0
         instance.y = 0
         instance.update(**dictionary)
