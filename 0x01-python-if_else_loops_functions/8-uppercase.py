#!/usr/bin/python3

def uppercase(str):
    for char in str:
        unicode_char = ord(char)
        if unicode_char >= 97 and unicode_char <= 122:
            unicode_char -= 32
        print("{:c}".format(unicode_char), end="")
    print()
