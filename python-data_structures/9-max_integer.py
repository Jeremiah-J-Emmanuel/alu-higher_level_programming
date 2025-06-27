#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        my_list.sort(reverse=True)
        return (my_list[0])


if __name__ == "__main__":
    print("This is the main")
