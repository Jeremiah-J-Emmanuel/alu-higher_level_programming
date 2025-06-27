#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return []
    else:
        try:
            new_list = my_list[:]
            count = 1
            for i in new_list:
                if i == search:
                    idx = new_list[count]
                    new_list[count] = replace
                    count = count + 1
                else:
                    count = count + 1
            return new_list
        except ValueError:
            return my_list


if __name__ == "__main__":
    search_replace(my_list, search, replace)
