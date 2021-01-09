#!/usr/bin/python3


"""
divides all the elements of a matrix

Function example:
    >>>matrix_divided([[3, 4, 9],[4, 3, 5],[9, 0, 3]], 2)
    [[1, 2, 4], [2, 1, 2], [4, 0, 1]]
"""


def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if len(matrix) > 1:
        x = len(matrix[0])
        for i in matrix:
            if len(i) != x:
                raise TypeError("Each row of the matrix must have \
the same size")
    new = []
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        new.append(list(map(lambda i: round(i / div, 2), i)))

    return new
