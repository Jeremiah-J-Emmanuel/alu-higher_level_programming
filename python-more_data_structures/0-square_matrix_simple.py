#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []

    if len(matrix) == 0:
        return matrix

    for i in matrix:
        if len(i) == 0:
            return(i)
        else:
            strapping = []
            for j in i:
                sqr = j ** 2
                strapping.append(sqr)
            new_list.append(strapping)
  
    return(new_list)


if __name__ == "__main__":
    square_matrix_simple(matrix=[])
