#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print('{}'.format(my_list[i]), end='')
            i += 1
        if x > 0:
            print()
    except IndexError:
        if len(my_list) != 0:
            print()
    return i
