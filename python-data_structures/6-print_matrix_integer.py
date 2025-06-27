#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            count = len(i) -
            if i.index(j) > count - 2:
                print("{}".format(j), end=" ")
            elif count == len(i)            :
                print("{}".format(j))


print_matrix_integer(matrix=[[1,2,3], [1,5,3], [1,4,5]])