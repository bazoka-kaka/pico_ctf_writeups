# Basic Mod 2

## Problem

A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Solve

Here's the solver script

```py
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
```

flag: picoCTF{1nv3r53ly_h4rd_8a05d939}
