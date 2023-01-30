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
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''
        calculates area of the square
        '''

        return self.__size ** 2

    def my_print(self):
        '''
        prints square using #
        '''

        if self.__size == 0:
            print()
        else:
            for a in range(self.size):
                for b in range(self.size):
                    print("#", end="")
                print()
