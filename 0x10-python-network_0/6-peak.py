#!/usr/bin/python3
"""function find pek module"""


def find_peak(list_of_integers):
    """Calculates a peak of a list"""
    if len(list_of_integers) == 0:
        return None
    nums = list_of_integers
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low + 1) // 2
        if mid - 1 >= 0 and nums[mid - 1] <= nums[mid]:
            low = mid
        else:
            high = mid - 1
    return nums[high]
