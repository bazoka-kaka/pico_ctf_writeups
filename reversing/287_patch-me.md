# PatchMe

## Problem
Can you get the flag? Run this Python program in the same directory as this encrypted flag.

## Solution

at the bottom of the script

```
# level_1_pw_check()
decryption = str_xor(flag_enc.decode(), "utilitarian")
print(decryption)
```

flag: picoCTF{p47ch1ng_l1f3_h4ck_f01eabfa}