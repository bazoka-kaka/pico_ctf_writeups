# Keygenme

## Problem

no description

## Solution

```
username_trial = b"FREEMAN"
r = hashlib.sha256(username_trial).hexdigest()
dynamic = key = r[4] + r[5] + r[3] + r[6] + r[2] + r[7] + r[1] + r[8]
print(dynamic)
```

output: 0d208392

flag: picoCTF{1n_7h3_|<3y_of_0d208392}