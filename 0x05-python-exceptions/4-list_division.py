#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    if list_length <= 0 or (len(my_list_1) == 0 and len(my_list_2) == 0):
        return []
    re_list = [0] * max(len(my_list_1), len(my_list_2))
    while i < list_length:
        try:
            re_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            re_list[i] = 0
        except ZeroDivisionError:
            print("division by 0")
            re_list[i] = 0
        except IndexError:
            print("out of range")
            re_list[i] = 0
        finally:
            i += 1
    return re_list
