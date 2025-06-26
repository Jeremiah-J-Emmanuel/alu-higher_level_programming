#!/usr/bin/python3
from calculator_1.py import add(a, b)
from calculator_1.py import sub(a, b)
from calculator_1.py import mul(a, b)
from calculator_1.py import div(a, b)

def main():
    a = 10
    b = 5

    added = add(a, b)
    multied = mul(a, b)
    divided = div(a, b)
    subtracted = sub(a, b)

    print("{} + {} = {}".format(a, b, added))
    print("{} - {} = {}".format(a, b, subtracted))
    print("{} * {} = {}".format(a, b, multied))
    print("{} / {} = {}".format(a, b, divided))

    return added, multied, subtracted, divided
