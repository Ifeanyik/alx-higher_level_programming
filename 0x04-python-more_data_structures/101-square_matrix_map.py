#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda i: [i[0] ** 2, i[1] ** 2, i[2] ** 2], matrix))
