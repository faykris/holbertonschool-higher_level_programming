#!/usr/bin/python3
def remove_char_at(str, n):
        cpy = ""
        i = 0
        if n < 0:
                return (str)
        for c in str:
                if i == n:
                        cpy = str[:n]
                        cpy = cpy + str[n + 1:]
                        break
                i += 1
        if i < n:
                return (str)
        else:
                return (cpy)
