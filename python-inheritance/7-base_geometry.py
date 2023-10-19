#!/usr/bin/python3
"""Create a class base geometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """unimplemented area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks the type and if negative for value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.name = name
            self.value = value
