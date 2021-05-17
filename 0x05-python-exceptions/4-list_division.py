#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    te = "wrong type"
    ze = "division by 0"
    ie = "out of range"
    if len(my_list_1) > len(my_list_2):
        re_list = [0] * len(my_list_1)
    else:
        re_list = [0] * len(my_list_2)
    while i < list_length:
        try:
            re_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("{}".format(te))
            re_list[i] = 0
        except ZeroDivisionError:
            print("{}".format(ze))
            re_list[i] = 0
        except IndexError:
            print("{}".format(ie))
            re_list[i] = 0
        finally:
            i += 1
    return re_list
