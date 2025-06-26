#!/usr/bin/python3

from sys import argv
def main():

    length = len(argv)

    if length == 0:
        print("0 arguments.")

    else:
        print(f"{length} argument:")
        count = 1
        while count <= length:
            item = argv[(count - 1)]
            print (f"{count}: {item}")
            count = count + 1

main()