#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        small_list = []
        for j in i:
            small_list.append(j**2)
        new_matrix.append(small_list)
    return new_matrix
