#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique = []
    for i in set_1:
        if not i in set_2:
            unique.append(i)
        else:
            pass
    for i in set_2:
        if not i in set_1:
            unique.append(i)
        else:
            pass
    return unique


if __name__ == "__main__":
    print("Yes")
