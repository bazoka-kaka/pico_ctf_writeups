#!/usr/bin/env python3

import string

f = open("message.txt")

str_val = f.read()

nums = [int(n) % 37 for n in str_val.split()]

flag = []

for n in nums:
  if n in range(26):
    flag.append(string.ascii_uppercase[n])
  elif n in range(26, 35):
    flag.append(string.digits[n - 26])
  else:
    flag.append('_')

print('picoCTF{' + ''.join(flag) + '}')