#!/usr/bin/python3
def print_last_digit(num):
    value = abs(num)
    last = value % 10
    if num > 0:
        print ("{}".format(last), end="")
    else:
        print ("-{}".format(last), end="")
