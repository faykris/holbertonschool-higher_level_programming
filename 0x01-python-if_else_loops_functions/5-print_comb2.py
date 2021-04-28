#!/usr/bin/python3
for i in range(0, 10):
        for j in range(0, 10):
                print("{:d}{:d}".format(i, j), end="")
                if i != 9 or j != 9:
                        print(", ", end="")
                else:
                        print("")
