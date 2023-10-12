#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square Class"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets size"""
        return self.__size

    @property
    def position(self):
        """Gets position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Sets the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
            not isinstance(value[0], int) or not isinstance(value[1], int) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
