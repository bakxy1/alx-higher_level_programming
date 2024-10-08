#!/usr/bin/python3
"""Module defines class `Rectangle`"""

from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(width) is not int:
            raise TypeError(f"width must be an integer")
        elif width <= 0:
            raise ValueError(f"width must be > 0")
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
        if type(height) is not int:
            raise TypeError(f"height must be an integer")
        elif height <= 0:
            raise ValueError(f"height must be > 0")
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
        if type(x) is not int:
            raise TypeError(f"x must be an integer")
        elif x < 0:
            raise ValueError(f"x must be >= 0")
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
        if type(y) is not int:
            raise TypeError(f"y must be an integer")
        elif y < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = y

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def display(self):
        """Displays rectangle in stdout"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Overrides string method for this class"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} "
            + f"- {self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """Updates attributes"""
        if len(args) > 0:
            for idx in range(len(args)):
                if idx == 0:
                    self.id = args[idx]
                elif idx == 1:
                    self.width = args[idx]
                elif idx == 2:
                    self.height = args[idx]
                elif idx == 3:
                    self.x = args[idx]
                elif idx == 4:
                    self.y = args[idx]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dict of object"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
