#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for i in set_1:
        if i in set_1 and i in set_2:
            common.append(i)
        else:
            pass
    return common


if __name__ == "__main__":
    print("Yes")
