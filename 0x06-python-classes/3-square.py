#!/usr/bin/python3
'''
Created on Mon Jan 30 2023
Author: Chibuokem Obiegbulem
'''


class Square:
    '''
    class Square that defines a square
    '''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''
        calculates area of the square
        '''

        return self.__size ** 2
