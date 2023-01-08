#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_strings = []
        for i in row:
            row_strings.append("{:d}".format(i))
            print("\t".join(row_strings))
