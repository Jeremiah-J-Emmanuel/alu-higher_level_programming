#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError or TypeError:
        return False


if __name__ == "__main__":
    print(safe_print_integer([1,2,4,4]))
