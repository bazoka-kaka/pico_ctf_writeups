#!/usr/bin/env python3

f = open('message.txt')

encrypted = f.read()

decoded = []

for i in range(0, len(encrypted), 3):
    a, b, c = encrypted[i:i+3]
    decoded.append(c+a+b)

flag = "".join(decoded).split(' ')[3]

print(flag)

f.close()