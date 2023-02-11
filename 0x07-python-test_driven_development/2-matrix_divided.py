#!/usr/bin/python3
"""
    This is the divide module.
    it divides the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix
    Args:
        matrix: intial 2D list
        div: integer which is the divisor
    Returns:
        New matrix containing the divided elements
        rounded to 2 decimal places
    """
    if not (isinstance(matrix, (int, float)) for lst in matrix for i in lst):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (len(matrix[0])) = len(lst) for lst in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(div, (int, float):
        raise TypeError("div must be a number")
    if div = 0:
    raise ZeroDivisionError("division by zero")
    return [[round(i / div) for i in lst] for lst in matrix]
