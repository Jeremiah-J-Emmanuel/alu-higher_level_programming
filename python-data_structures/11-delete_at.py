#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    range = len(my_list) - 1
    if idx > range or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
if __name__ == "__main__":
    print(delete_at(my_list=[3, 5, 6], idx=2))
