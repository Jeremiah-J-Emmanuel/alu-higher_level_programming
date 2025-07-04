#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(my_list[14])
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    print(safe_print_integer({}))
