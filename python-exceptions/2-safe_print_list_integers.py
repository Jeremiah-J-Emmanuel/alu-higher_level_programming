#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_list = []
    for i in my_list:
        count = 1 #for returning the number of int printed
        try:
            if my_list.index(i) < x:
                print("{:d}".format(i), end=" ")
                int_list.append(i)
                count = count + 1
            else:
                print(*["{:d}".format(i)])
                int_list.append(i)
                count = count + 1
        except ValueError:
                pass
    return count


if __name__  == "__main__":
    safe_print_list_integers(my_list=[1,2, 3,4, 5, "Hello", 4, 6], x=9\
)