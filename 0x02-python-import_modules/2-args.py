#!/usr/bin/python3
import sys
if __name__ == "__main__":
    lenarg = len(sys.argv) - 1
    if len(sys.argv) == 1:
        print("{} arguments.".format(lenarg))
    elif len(sys.argv) == 2:
        print("{} argument:".format(lenarg))
        for i, arg in enumerate(sys.argv):
            if i != 0:
                print("{}: {}".format(i, arg))
    else:
        print("{} arguments:".format(lenarg))
        for i, arg in enumerate(sys.argv):
            if i != 0:
                print("{}: {}".format(i, arg))
