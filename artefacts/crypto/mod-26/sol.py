#!/usr/bin/env python3

import string

f = open("encrypted.txt")

encrypted = f.read()

decrypted = []

for x in encrypted:
    if x.isalpha():
        if x.isupper():
            decrypted.append(string.ascii_uppercase[(string.ascii_uppercase.index(x) + 13) % 26])
        else:
            decrypted.append(string.ascii_lowercase[(string.ascii_lowercase.index(x) + 13) % 26])
    else:
        decrypted.append(x)

print("".join(decrypted))

f.close()