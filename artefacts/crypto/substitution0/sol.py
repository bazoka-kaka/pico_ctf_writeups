#!/usr/bin/env python3

import string

f = open("message.txt")

content = f.read()
key = content.split(' ')[0]
d_flag = content.split('\n')[-1].split(' ')[-1]

decrypted = []

for x in d_flag:
    if x in ['{', '}', '_'] or x.isnumeric():
        decrypted.append(x)
    else:
        i = key.index(x.upper())
        decrypted.append(string.ascii_uppercase[i])

print("".join(decrypted))

f.close()