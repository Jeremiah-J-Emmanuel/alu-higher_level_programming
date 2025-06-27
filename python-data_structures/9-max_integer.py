#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        my_list.sort(reverse=True)
        return (my_list[0])


if __name__ == "__main__":
    max_integer([1,35,3,5,2])
