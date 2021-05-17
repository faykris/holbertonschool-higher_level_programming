#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            printed += 1
        except ValueError:
            print(end="")
        except TypeError:
            print(end="")
        except IndexError:
            print(end="")
        i += 1
    if x > 0:
        print()
    return printed
