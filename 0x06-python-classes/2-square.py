#!/usr/bin/python3
""" A module defining a square"""


class Square:
    """A class rep'ing a square"""

    def __init__(self, size=0):
        """ Initialise Square class
        Args:
            size: rep size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
