# Substitution 0

## Problem

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message here.

## Solution

just use the following script:

```
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
```

Here's the flag: `PICOCTF{5UB5717U710N_3V0LU710N_357BF9FF}`
