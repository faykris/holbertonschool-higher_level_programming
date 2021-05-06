#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    if len(my_list) == 0:
        return
    new_list = list(" " * len(my_list))
    i = 0
    for ele in my_list:
        if ele == search:
            new_list[i] = replace
        else:
            new_list[i] = my_list[i]
        i += 1
    return new_list
