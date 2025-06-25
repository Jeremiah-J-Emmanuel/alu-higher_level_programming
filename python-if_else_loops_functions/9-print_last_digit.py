#!/usr/bin/python3
def print_last_digit(num):
    value = abs(num)
    last = value % 10
    print("{}".format(last), end="")