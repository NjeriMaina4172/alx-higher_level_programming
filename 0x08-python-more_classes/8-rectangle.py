#!/usr/bin/python3
"""creating the Rectangle class"""


class Rectangle:
    """ initializing the recatngle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """ setting the Rctangle variables
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ a function to return the area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ a method to return the perimeter of the rectangle
        if the height or the width of the rectangle is zero,
        then the perimeter is equal to zero"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__width) + (2 * self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the rectangle witht the bigger area
        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle
        Raises:
            TypeError: if either rect_1 or rect_2 is not a rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """ a function to return the printable representation
        of the rectangle
        represents the rectangle with # """

        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """ return the string reoresentation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ printing a message for every delition"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
        