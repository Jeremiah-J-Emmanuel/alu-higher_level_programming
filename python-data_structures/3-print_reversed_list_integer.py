#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse=True)

    for i in my_list:
        print("{}".format(i))


if __name__ == "__main__":
    print_reversed_list_integer(my_list=[])
