#!/usr/bin/python3
def uppercase(str):
	new = ""
	for i in str:
		if ord(i) in range(97,123):
			j =  chr(ord(i) - 32)
			new = new + j
		else:
			new = new + i
	print (new)

