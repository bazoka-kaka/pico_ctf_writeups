#!/usr/bin/env python3

f = open("message.txt", "r")

data = f.read()

flag = []

for i in range(0, len(data), 3):
  content = data[i:i+3]
  a, b, c = content
  flag.append(c + a + b)

complete = "".join(flag)

print(complete.split(' ')[3])