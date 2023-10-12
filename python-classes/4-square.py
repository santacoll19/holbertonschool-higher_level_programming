#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""

    def __init__(self, size=0):
        """Initialize sqr"""
        if type(size) is not int:
            raise ValueError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

    @property
    def size(self):
        """Getter of size"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """set the sqr size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = value

    def area(self):
        """Return square area"""
        return self._Square__size ** 2
