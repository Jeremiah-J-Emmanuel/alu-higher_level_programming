#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_data = {key: value}
    a_dictionary.update(new_data)
    return a_dictionary

if __name__ == "__main__":
    print("")
