#!/usr/bin/python3
"""Square class inherited from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class"""

    def __init__(self, size):
        """Initializes values"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates area"""
        return (self.__size * self.__size)
