#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div(a, b)

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
if __name__ == "__main__":
    main()
