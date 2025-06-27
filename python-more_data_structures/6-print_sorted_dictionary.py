#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict_list = sorted(a_dictionary.items())
    sorted_dict = dict(sorted_dict_list)
    for key in sorted_dict:
        val = a_dictionary[key]
        print(f"{key} : {val}")


if __name__ == "__main__":
    print("Yes")
