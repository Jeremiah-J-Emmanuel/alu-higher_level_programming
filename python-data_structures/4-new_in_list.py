#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    range = len(new_list) - 1
    idx = int(idx)

    if idx < 0:
        return my_list
    if idx > range:
        return my_list
    else:
        new_list[idx] = element
        return new_list


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
