#!/usr/bin/python3
""" 1. Divide a matrix
    Module Task 1
    Write a function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """ matrix_divided - function
        Args:
            matrix: matrix to be divided in their elements
            div: number to divide each element of the matrix
        Returns:
            a new matrix with divided values
    """
    i = 0
    j = 0
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"
    c_a = []
    c_m = []
    size = 0
    if type(div) != int and type(div) != float:
        raise TypeError(err3)
    if div == 0 or div == 0.0:
        raise ZeroDivisionError(err4)

    for j in range(len(matrix[0])):
        c_a.append(0)
        size = j + 1
    for i in range(len(matrix)):
        c_m.append(list(c_a))

    i = j = 0
    for row in matrix:
        if type(row) != list:
            raise TypeError(err1)
        for col in row:
            if len(row) != size:
                raise TypeError(err2)
            if type(col) != int and type(col) != float:
                raise TypeError(err1)
            c_m[i][j] = round(col / div, 2)
            j += 1
        j = 0
        i += 1
    return c_m
