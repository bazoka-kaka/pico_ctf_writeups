# Substitution 0

## Problem

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? Download the message here.

## Solution

just use the following script:

```
#!/usr/bin/env python3

import string

file = open("message.txt", "r")
data = file.read()

upper_key = data[:27]
lower_key = upper_key.lower()
content = data[29:]

decoded = []

for idx, x in enumerate(content):
  if x.islower():
    i = lower_key.index(x)
    decoded.append(string.ascii_lowercase[i])
  elif x.isupper():
    i = upper_key.index(x)
    decoded.append(string.ascii_uppercase[i])
  else:
    decoded.append(x)

flag = ''.join(decoded).split(': ')[1]
print(flag)
```

Here's the flag: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}
