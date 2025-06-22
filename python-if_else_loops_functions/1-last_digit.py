#!/usr/bin/bash
import random
number = random.randint(-10000, 10000)
number = str(number)
last = int(number[-1])
base_text = f"last digit of {number} is {number[-1]} and is"

if last > 5:
	print (base_text, "greater than 5")
elif last == 0:
	print (base_text, "0")
else:
	print (base_text, "less than six and not 0")
