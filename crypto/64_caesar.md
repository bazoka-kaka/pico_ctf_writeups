# Caesar

## Problem

Decrypt this message.

encrypted: picoCTF{ynkooejcpdanqxeykjrbdofgkq}

## Solution

create the following python script:

```py
#!/usr/bin/env python3

import re
import string

f = open("ciphertext", "r")

content = f.read()

# get only the encrypted content
enc = re.findall("{.*?}", content)[0][1:-1]

# convert to int
enc_int = [string.ascii_lowercase.index(x) + 1 for x in enc]

# results
results = []

# searching for all the possible ROTs
for i in range(1, 26):
    flag = []
    for l in enc_int:
        flag.append(string.ascii_lowercase[(l + i) % 26])
    possible_flag = "".join(flag)
    print(possible_flag)
    results.append(possible_flag)
    
print()

# the possible ROT is the 3rd one (ROT3)
print("picoCTF{" + results[2] + "}")

f.close()
```

FLAG: `picoCTF{crossingtherubiconvfhsjkou}`