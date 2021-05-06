#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b_list = list(" " * len(my_list))
    i = 0
    for ele in my_list:
        if ele % 2 == 0:
            b_list[i] = True
        else:
            b_list[i] = False
        i += 1
    return b_list
