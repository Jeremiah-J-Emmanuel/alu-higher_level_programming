#!/usr/bin/python3
def search_replace(my_list, search, replace):
    try:
        new_list = my_list 
        idx = new_list.index(search)
        new_list[idx] = replace
        return my_list
    except IndexError:
        return []


if __name__ == "__main__":
    search_replace(my_list, search, replace)
