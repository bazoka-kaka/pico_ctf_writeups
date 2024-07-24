# The Numbers

## Problem

The numbers... what do they mean?

## Solution

1. convert the numbers in the image to .txt format `16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }`
2. Create the following python decryption script

```py
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

```

FLAG: `picoctf{thenumbersmason}`
