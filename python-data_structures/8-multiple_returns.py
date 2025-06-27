#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        length = len(sentence)
        first = None
        tup1 = (length, first)
        return tup1
    else:
        length = len(sentence)
        first = sentence[0]
        tup1 = (length, first)
        return tup1


if __name__ == "__main__":
    print(multiple_returns(sentence))
