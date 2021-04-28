#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv):
            if i != 0:
                print(f"{i}: {arg}")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv):
            if i != 0:
                print(f"{i}: {arg}")
