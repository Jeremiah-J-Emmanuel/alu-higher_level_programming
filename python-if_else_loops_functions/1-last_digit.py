#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
base_text = f"Last digit of {number} is {last} and is"

if number < 0:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
elif last > 5:
    print(base_text, "greater than 5")
elif last == 0:
    print(base_text, "0")
else:
    print(base_text, "less than 6 and not 0")
