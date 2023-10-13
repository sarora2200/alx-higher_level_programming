#!/usr/bin/python3
"""Modules for class base
It takes a private instance object
"""
import json
import os
import csv
import turtle


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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.jason".format(cls.__name__)
        if not os.path.exists(filename):
            return []

        ret = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
            ret = [cls.create(**d) for d in list_dicts]
        return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes to csv a list of instances"""
        if list_objs is None:
            list_objs = []

        filename = "{}.csv".format(cls.__name__)
        attrs = ('id', 'size', 'width', 'height', 'x', 'y')
        with open(filename, "w", encoding="utf-8") as f:
            for o in list_objs:
                d = o.to_dictionary()
                t = []
                for attr in attrs:
                    if attr not in d:
                        continue
                    t.append(str(d.get(attr)))
                f.write(",".join(t))
                f.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """deserializes CSV"""
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                arguments = line[:-1].split(",")
                o = cls(1, 1)
                o.update(*[int(x) for x in arguments])
                list_objs.append(o)
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
