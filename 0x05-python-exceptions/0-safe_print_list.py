#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if x <= 0 or len(my_list) == 0:
        return 0
    try:
        while i < x:
            print('{}'.format(my_list[i]), end='')
            i += 1
        if x > 0:
            print()
    except IndexError:
        print()
    return i
