#!/usr/bin/python3
""" Rectangle module"""


from models.base import Base


class Rectangle(Base):
    """ REctangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """intialization method"""
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.__y = value

    def area(self):
        """area method"""
        return self.width * self.height

    def display(self):
        """display method"""
        for lines in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """string representation of rectangle"""
        r = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        c = "{}/{} - {}/{}".format(
                self.x, self.y, self.width, self.height)
        return r + c

    def update(self, *args):
        """update method"""
        if args or len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(
                                self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            if kwargs or len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value
