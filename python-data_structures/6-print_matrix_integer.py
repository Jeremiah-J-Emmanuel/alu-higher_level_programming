#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) == 0:
            print("")
        else:
            for j in i:
                range = len(i) - 1
                if i.index(j) < range:
                    print("{:d}".format(j), end=" ")
                else:
                    print("{:d}".format(j))


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
