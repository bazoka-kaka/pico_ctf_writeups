#!/usr/bin/env python3

import re
import string

f = open("ciphertext")

content = f.read()

encrypted = re.findall("{.*?}", content)[0][1:-1]

for i in range(1, 27):
    decrypted = ""
    for x in encrypted:
        if x.isalpha():
            decrypted += string.ascii_lowercase[(string.ascii_lowercase.index(x) + i) % 26]
        else:
            decrypted += x
    if i == 4:
        print("picoCTF{" + decrypted + "}")

f.close()