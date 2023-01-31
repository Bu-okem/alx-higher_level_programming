#!/usr/bin/python3
'''
Created on Mon Jan 30 2023
Author: Chibuokem Obiegbulem
'''


class Square:
    '''
    class Square that defines a square
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
