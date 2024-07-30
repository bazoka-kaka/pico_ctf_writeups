#!/usr/bin/env python3

f = open("flag.txt")

flag = "".join([chr(int(x)) for x in f.read().split(' ')])

print(flag)

f.close()