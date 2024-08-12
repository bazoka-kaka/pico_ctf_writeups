#!/usr/bin/env python3

import string

f = open("ciphertext")

encrypted = f.read()

decrypted = ""

for x in encrypted:
    if x.isalpha():
        if x.isupper():
            decrypted += string.ascii_uppercase[(string.ascii_uppercase.index(x) + 13) % 26]
        else:
            decrypted += string.ascii_lowercase[(string.ascii_lowercase.index(x) + 13) % 26]
    else:
        decrypted += x

print(decrypted)

f.close()