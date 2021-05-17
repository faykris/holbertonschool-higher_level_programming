#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if x <= 0 or my_list == []:
        return i
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
    except IndexError:
        print(end="")
    print("")
    return i
