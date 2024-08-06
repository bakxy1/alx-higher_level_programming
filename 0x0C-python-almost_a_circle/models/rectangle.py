#!/usr/bin/python3
"""Module defines class `Rectangle`"""

from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter of width prop"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter of width prop

        Args:
            width: New width to set

        Returns:
            None
        """
        self.__width = width

    @property
    def height(self):
        """Getter of height prop"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter of height prop

        Args:
            width: New height to set

        Returns:
            None
        """
        self.__height = height

    @property
    def x(self):
        """Getter of x prop"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter of x prop

        Args:
            width: New x to set

        Returns:
            None
        """
        self.__x = x

    @property
    def y(self):
        """Getter of y prop"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter of y prop

        Args:
            width: New y to set

        Returns:
            None
        """
        self.__y = y
