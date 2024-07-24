#!/usr/bin/env python3

import string

f = open("enc.txt", "r")

enc = f.read()

arr = enc.split(" ")

flag = []

for l in arr:
	if l.isnumeric():
		flag.append(string.ascii_lowercase[int(l) - 1])
	else:
		flag.append(l)

print("".join(flag))

f.close()
