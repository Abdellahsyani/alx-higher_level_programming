#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''the function to store matrix'''
    for row in matrix:
        for colum in row:
            print("{:d}".format(colum), end=" " if colum != row[-1] else "")
        print()
