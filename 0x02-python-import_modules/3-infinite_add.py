#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lenarg = len(sys.argv) - 1
    num = 0
    if lenarg == 0:
        print("{}".format(lenarg))
    elif lenarg == 1:
        print("{}".format(sys.argv[1]))
    else:
        for i, arg in enumerate(sys.argv):
            if i != 0:
                num = num + int(sys.argv[i])
        print("{}".format(num))
