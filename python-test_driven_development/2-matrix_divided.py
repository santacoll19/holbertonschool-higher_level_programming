#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """>>> matrix_divided([[]], 3)
[[]]
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], -2)
[[-0.5, -1.0, -1.5], [-2.0, -2.5, -3.0]]
>>> matrix_divided([[1.5, 2.8, 3.3], [4.2, 5.5, 6.6]], 2)
[[0.75, 1.4, 1.65], [2.1, 2.75, 3.3]]
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
