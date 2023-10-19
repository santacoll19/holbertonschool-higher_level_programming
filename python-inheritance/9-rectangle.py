#!/usr/bin/python3
"""Rectangle class inherited from BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherited from BaseGeometry class"""

    def __init__(self, width, height):
        """Rectangle class inherited from BaseGeometry class"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """Rectangle class inherited from BaseGeometry class"""
        return self.__width * self.__height

    def __str__(self):
        """Rectangle class inherited from BaseGeometry class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
