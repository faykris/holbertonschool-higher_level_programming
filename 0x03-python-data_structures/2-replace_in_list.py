#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    new_list = my_list

    if idx < 0 or idx > len(my_list):
        return my_list
    while i < len(my_list):
        if i == idx:
            new_list[i] = element
        else:
            new_list[i] = my_list[i]
        i += 1
    return new_list
