#!/usr/bin/python3
def roman_to_int(roman_string):
    r_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    i = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    if not roman_string:
        return 0
    while i < len(roman_string):
        s1 = r_nums[roman_string[i]]
        if i + 1 < len(roman_string):
            s2 = r_nums[roman_string[i + 1]]
            if s1 >= s2:
                total = total + s1
                i = i + 1
            else:
                total = total - s1
                i = i + 1
        else:
            total = total + s1
            i = i + 1
    return total
