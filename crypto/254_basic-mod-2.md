# Basic Mod 2

## Problem

A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Solve

Here's the solver script

```
#!/usr/bin/env python3

import string

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

f = open("message.txt", 'r')

data = f.read()

arr = [modinv(int(val), 41) for val in data.split()]

flag = []

for n in arr:
  if n in range(27):
    flag.append(string.ascii_letters[n - 1])
  elif n in range(27, 37):
    flag.append(string.digits[n - 27])
  else:
    flag.append('_')

print("picoCTF{" + "".join(flag) + "}")
```

flag: picoCTF{1nv3r53ly_h4rd_8a05d939}
