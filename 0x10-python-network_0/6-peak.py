#!/usr/bin/python3
"""function find pek module"""


def find_peak(list_of_integers):
    """Calculates a peak of a list"""
    if not list_of_integers or type(list_of_integers) != list:
        return None
    n = len(list_of_integers)
    n_list = list_of_integers
    if n == 1:
        return n_list[0]
    if n_list[n - 1] >= n_list[n - 2]:
        return n_list[n - 1]
    for i in range(1, n - 1):
        if n_list[i] >= n_list[i - 1] and n_list[i] >= n_list[i + 1]:
            return n_list[i]
