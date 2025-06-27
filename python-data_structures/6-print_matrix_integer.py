#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            range = len(i) - 1
            if i.index(j) < range:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))


if __name__ == "__main__":
    print_matrix_integer(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
