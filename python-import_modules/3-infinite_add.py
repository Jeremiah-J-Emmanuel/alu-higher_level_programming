#!/usr/bin/python3
from sys import argv


def main():
    count = 0
    for i in argv[1:]:
        i = int(i)
        count = count + i

    print(count)


if __name__ == "__main__":
    main()

