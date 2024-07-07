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