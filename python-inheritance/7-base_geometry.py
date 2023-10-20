#!/usr/bin/python3
"""Write a class BaseGeometry."""


class BaseGeometry():
    """BaseGeometry class
    """

    def area(self):
        """Public instance method

        Raises:
            Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that that validates value

        Raises:
            TypeError: if value is not an integer
            with the message <name> must be an integer
            ValueError: if value is less or equal to 0
            with the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.name = name
            self.value = value
