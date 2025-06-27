#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict_list = sorted(a_dictionary.items())
    sorted_dict = dict(sorted_dict_list)
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print("Yes")
