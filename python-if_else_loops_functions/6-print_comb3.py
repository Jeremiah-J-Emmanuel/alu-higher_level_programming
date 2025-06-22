#!/usr/bin/python3
out = []
for n in range(100):
	if n < 10:
        	out.append(f"0{n}")
	else:
		padded = []
        	padded.append(f"{str(n)}")
		hold.append(f"{(padded[0])[0]}")
		hold.append(f"{(padded[0])[1]}")
		hold.sort()
	if (hold[0] + hold[1]) in out:
		continue
	else:
		out.append(hold[0] + hold[1])
]

for i in out:
	print (i, sep = ", ")
