#!/usr/bin/python3
'''Function to divide all elements of a matrix by a given integer'''


def matrix_divided(matrix, div):
    '''This function divides elements of a list of lists of integers or floats'''        
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if int != type(div) != float:
        raise TypeError("div must be a number")
    new_matrix = []
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            new_matrix_el = []
            for j in i:
                if type(j) != int and type(j) != float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                else:
                    new_matrix_el.append(round(j/div, 2))
        new_matrix.append(new_matrix_el)
    for k in range(len(new_matrix)):
        if k < len(new_matrix) - 1:
            if len(new_matrix[k]) != len(new_matrix[k + 1]):
                raise TypeError("Each row of the matrix must have the same size")
        else:
            break
    return new_matrix
