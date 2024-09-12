#!/usr/bin/python3
"""
Function that divides all elements of a matrix
Checks for TypeError and ZeroDivisonError.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix rounded to 2 decimal places.

    Args:
        matrix (list of lists of integers or floats):
          List of lists containing integers or floats.
        div (integer or float):
          Must be a number different from 0.

    Returns:
        New matrix (new_matrix) with all elements
          of the original matrix divided
            by div rounded to 2 decimal places.

    Raises:
        TypeError:
            If matrix is not a list of lists of integers or floats.
            If each row of the matrix is not the same size.
            If div is not an integer or a float.

        ZeroDivisionError: If div is 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a \
                        matrix (list of lists) of integers/floats")
    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
