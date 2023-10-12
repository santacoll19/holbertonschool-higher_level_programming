#!/usr/bin/python3
"""This module contains a square class"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Property"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            return self.__position

    def area(self):
        """generates the area"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for z in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
