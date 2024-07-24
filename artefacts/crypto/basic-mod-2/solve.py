#!/usr/bin/env python3

import string

f = open("message.txt")

content = f.read()

# modular inverse the contents
enc = [pow(int(x), -1, 41) for x in content.split(' ')]

flag = []

for x in enc:
    if x in range(1, 27):
        flag.append(string.ascii_lowercase[x - 1])
    elif x in range(27, 37):
        flag.append(str(x % 26 - 1))
    else:
        flag.append("_")

print("picoCTF{" + "".join(flag) + "}")

f.close()