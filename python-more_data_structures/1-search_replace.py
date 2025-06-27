#!/usr/bin/python3
def search_replace(my_list, search, replace):
    try:
        idx = my_list.index(search)
        my_list[idx] = replace
        return my_list
    except IndexError:
        return []


if __name__ == "__main__":
    search_replace(my_list, search, replace)
