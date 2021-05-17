#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    em_list = []
    if my_list == em_list:
        print("")
        return 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except ValueError:
            print(end="")
        except TypeError:
            print(end="")
    if x > 0:
        print()
    return printed
