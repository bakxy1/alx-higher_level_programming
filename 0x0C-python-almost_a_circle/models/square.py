#!/usr/bin/python3
"""Module defines class `Square`"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width, self.height = size, size

    def __str__(self):
        """Overrides Rectangle's string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " + f"- {self.width}"
