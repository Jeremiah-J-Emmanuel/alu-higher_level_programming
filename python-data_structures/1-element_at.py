#!/usr/bin/python3

def element_at(my_list, idx):
    idx = int(idx)
    range = (len(my_list) - 1)

    if idx < 0:
        return None
    elif idx > range:
        return None
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))


if __name__ == "__main__":
    element_at(my_list, idx)
