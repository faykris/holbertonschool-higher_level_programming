#!/usr/bin/python3
def uppercase(str):
        i = 0
        upp = ""
        cha = ""
        for s in str:
                if ord(s) >= 97 and ord(s) <= 122:
                        cha = chr(ord(s) - 32)
                        upp = upp + cha
                else:
                        upp = upp + s
                        i += 1
                print(upp)
