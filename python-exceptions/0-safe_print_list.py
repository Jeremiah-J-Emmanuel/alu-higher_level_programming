#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_list = []
    try:
        count = 0
        for i in my_list:
            count = count + 1
            if my_list.index(i) <= (x - 1):
                new_list.append(i)
    except IndexError:
        print(*new_list, sep="")
        return count
    
    print(*new_list, sep="")
    return count
    

print(safe_print_list(my_list=[1, 2, 4,5,6,], x=6))