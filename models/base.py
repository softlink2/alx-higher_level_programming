#!/usr/bin/python3
"""Defines the Base class"""


class Base:
    """The Base class
    This class is the “base” of all other classes in this project
    Private class attribute:
        __nb_objects (int):Number of Bases class instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base
        Args:
            id (int): The identity of the Base instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
