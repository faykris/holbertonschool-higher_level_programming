#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0:
        return "None"
    while i < len(my_list):
        if i - 1 == idx:
            return i
        i += 1
    return "None"
