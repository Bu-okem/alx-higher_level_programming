#!/usr/bin/python3

def best_score(a_dictionary):
    max_value = 0
    largest = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                largest = key
        return largest
