#!/usr/bin/python3

from sys import argv
def main():

    length = len(argv)

    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument.")
        print("1:", argv[1])
    else:
        real_len = length - 1
        print(f"{real_len} arguments:")
        count = 1
        while count <= real_len:
            item = argv[count]
            print (f"{count}: {item}")
            count = count + 1

if "__name__" == "__main__":
    main()