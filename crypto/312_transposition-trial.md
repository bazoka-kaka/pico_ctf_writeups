# Transposition Trial

## Problem

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message. Download the corrupted message here.

## Solution

Here's the script to complete the challenge:

```
#!/usr/bin/env python3

f = open("message.txt", "r")

data = f.read()

flag = []

for i in range(0, len(data), 3):
  content = data[i:i+3]
  a, b, c = content
  flag.append(c + a + b)

complete = "".join(flag)

print(complete.split(' ')[3])
```

here's the flag: picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
