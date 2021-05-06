#!/usr/bin/python3
def sqrt_matrix(matrix=[]):
    return matrix**2


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_m = [[" "] * len(matrix[0])] * len(matrix)
    i = 0
    for row in matrix:
        new_m[i] = list(map(sqrt_matrix, matrix[i]))
        i += 1
    return new_m
