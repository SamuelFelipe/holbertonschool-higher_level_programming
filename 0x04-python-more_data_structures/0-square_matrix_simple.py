#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for fl in matrix:
        new_fl = []
        for cl in fl:
            new_fl.append(cl * cl)
        new_matrix.append(new_fl)
    return new_matrix
