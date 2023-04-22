#!/usr/bin/python3
"""Class "Rectangle" inherits fron "Base" class.
With private instance attributes, each with its
own public getter and setter"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle instances
        Args:
            id(int):The Rectangle's identity
            width(int): Rectangle's width
            height(int): Rectangle's height
            x(int): The x coordinate of the rectangle
            y(int): The y coordinate of the rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """set/get the rectangle's width"""
            return self.__width

        @width.setter
        def width(self, value):
            pass

        @property
        def height(self):
            """set/get the rectangle's height"""
            return self.__height

        @height.setter
        def height(self, value):
            pass

        @property
        def x(self):
            """set/get the rectangle's 'x' coordinate"""
            return self.__x

        @x.setter
        def x(self, value):
            pass

        @property
        def y(self):
            """set/get the rectangle's 'y' coordinate"""
            return self.__y

        @y.setter
        def y(self, value):
            pass
