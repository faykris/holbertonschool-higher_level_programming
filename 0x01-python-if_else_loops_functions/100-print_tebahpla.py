#!/usr/bin/python3
c = 122
t = 0
while (c != 96):
        if c % 2 != 0:
                t = c
                print("{:c}".format(t-32), end="")
        else:
                print("{:c}".format(c), end="")
        c -= 1
