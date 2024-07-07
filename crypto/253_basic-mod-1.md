# Basic Mod 1

## Problem

We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message here. Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Solution

We just create a python script like the following:

```
#!/usr/bin/env python3

import string

flag = []

with open("message.txt") as filp:
  contents = filp.read()
  nums = [int(val) for val in contents.split()]
  for num in nums:
    mod = num % 37
    
    if mod in range(26):
      flag.append(string.ascii_uppercase[mod])
    elif mod in range(26, 36):
      flag.append(string.digits[mod - 26])
    else:
      flag.append('_')

print("picoCTF{" + ''.join(flag) + "}")
```

flag: picoCTF{R0UND_N_R0UND_B6B25531}