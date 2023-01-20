#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(mylist):
        return mylist

    mylist[idx] = element
    return mylist
