#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    nl = dir(hidden_4)
    nl.sort()
    for n in nl:
        if (n[:2] != "__"):
            print("{}".format(n))
