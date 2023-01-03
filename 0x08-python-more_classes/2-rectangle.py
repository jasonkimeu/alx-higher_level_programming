#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """init width and height"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            """raise typerror"""
            raise TypeError('height must be an integer')
        if value < 0:
            """raise valueerror"""
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            """raise typerror"""
            raise TypeError('width must be an integer')
        if value < 0:
            """raise valueerror"""
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """return rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """return perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
