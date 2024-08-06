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

    def update(self, *args, **kwargs):
        """Update attributes of square"""
        if len(args) > 0:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                elif idx == 1:
                    self.size = args[idx]
                elif idx == 2:
                    self.x = args[idx]
                elif idx == 3:
                    self.y = args[idx]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """Overrides Rectangle's string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " + f"- {self.width}"
