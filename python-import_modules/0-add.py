#!/usr/bin/python3
def main():
    from add_0.py import add(a, b)

    a = 1
    b = 2
    answer = add(a, b)
    print("{} + {} = {answer}".format(a, b, answer))

if "__name__" == "__main__":
    main()
