#!/usr/bin/python3
"""Class exercise concerning rectangles"""


class Rectangle:
    """This class creates rectangles"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init function"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """value of rectangle setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """return height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """value of rectangle setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """return are of rectangle"""
        area_rec = self.__height * self.__width
        return area_rec

    def perimeter(self):
        """retrieve perimeter of rec"""
        if self.__width == 0 or self.__height == 0:
            perimeter_rec = 0
            return perimeter_rec
        else:
            perimeter_rec = (self.__width * 2) + (self.__height * 2)
            return perimeter_rec

    def __str__(self):
        """return string of rec"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += str(self.print_symbol)
            rec += "\n"
        return rec[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
