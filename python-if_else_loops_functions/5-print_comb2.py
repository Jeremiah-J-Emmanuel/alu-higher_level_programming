#!/usr/bin/python3
for i in range(100):
    deci = i
    if i < 99:
        print("{:02}".format(deci), end=", ")
    else:
        print("{:02}".format(deci), end="\n")
