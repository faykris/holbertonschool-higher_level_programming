#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    j = 0
    k = 0
    le = 0
    for i in matrix:
        for k in matrix[j]:
            print("{:d}".format(k), end="")
            if len(i) - 1 != le:
                print(end=" ")
            le += 1
        le = 0
        print()
        j += 1
