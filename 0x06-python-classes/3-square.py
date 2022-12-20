#!/usr/bin/python3
""" A module called square.py file"""


class Square:
    """ A class defining square"""

    def __init__(self, size=0):
        """initialise Square class
        Args:
            size: private instance must be an integer
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise ValueError('size must be >= 0')
        if size < 0:
            raise TypeError('size must be an integer')
        self.__size = size

    def area(self):
        """area public method
        Args:
            self: current object
        Returns:
            current square area
        """
        return self.__size ** 2
