#!/usr/bin/python3
'''
Created on Tue Jan 31 2023
Author: Chibuokem Obiegbulem

This module provides a Rectangle class that represents a rectangle with
properties width and height, and methods area and perimeter for calculating
the area and perimeter of the rectangle, respectively. The width and height
of the rectangle must be integers, and can be set and retrieved through the
width and height properties. In case the width or height is set to a
non-integer value or a negative number, a TypeError or ValueError will be
raised, respectively
'''


class Rectangle:
    '''
    class that defines a rectangle
    '''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    def area(self)
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
