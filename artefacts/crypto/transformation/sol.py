#!/usr/bin/env python3

f = open("enc")

encoded = f.read()

decoded = []

for x in encoded:
    d1 = chr(ord(x) >> 8)
    d2 = chr(x.encode('utf-16be')[-1])
    decoded.append(d1)
    decoded.append(d2)

print("".join(decoded))

f.close()