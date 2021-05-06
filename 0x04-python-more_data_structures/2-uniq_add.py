#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    cm_list = list(set(my_list))
    return sum(cm_list)
