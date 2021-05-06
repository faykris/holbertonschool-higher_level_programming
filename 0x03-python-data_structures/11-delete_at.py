#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = list(" " * (len(my_list) - 1))
    i = 0
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    elif idx == 0:
        for ele in my_list:
            if i != len(my_list) - 1:
                new_list[i] = my_list[i + 1]
            i += 1
    elif idx == len(my_list) - 1:
        for ele in my_list:
            if i != len(my_list) - 1:
                new_list[i] = my_list[i]
            i += 1
    else:
        for ele in my_list:
            if i != len(my_list) - 1:
                new_list[i] = ele
            i += 1
    my_list = new_list
    return my_list
