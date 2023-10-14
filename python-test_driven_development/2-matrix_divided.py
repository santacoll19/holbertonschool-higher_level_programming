#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """matrix divided function"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(i) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if type(div) is float:
        div = round(div, 2)
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix
