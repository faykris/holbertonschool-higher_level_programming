#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dic = sorted(a_dictionary.items())
    for key, val in s_dic:
        print("{} {}".format(key, val))
