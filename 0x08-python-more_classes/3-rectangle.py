#!/usr/bin/python3
'''
Author: Chibuokem Obiegbulem
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

    def __str__(self):
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res

        for i in range(self.__height):
            if i == self.__height - 1:
                res += ('#' * self.__width)
            else:
                res += (('#' * self.__width) + '\n')
        return res
