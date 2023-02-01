#!/usr/bin/python3
'''
Author: Chibuokem Obiegbulem
'''

def add_integer(a, b=98):
    if type(a) is not int:
        if type(a) is float:
            int (a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float:
            int (b)
        else:
            raise TypeError("b must be an integer")
    return a + b
