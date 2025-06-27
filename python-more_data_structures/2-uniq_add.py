#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    for i in my_list:
        if i in uniq:
            pass
        else:
            uniq.append(i)
    add = 0
    for i in uniq:
        add = add + i
    return add


if __name__ == "__main__":
    print("Yes")
