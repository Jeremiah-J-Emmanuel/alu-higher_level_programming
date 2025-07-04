#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = (a / b)
    except (ZeroDivisionError, ValueError):
        ans = None
    finally:
        print("Inside result: {}".format(ans))
        return ans


if __name__ == "__main__":
    print(safe_print_division(2, 0))
