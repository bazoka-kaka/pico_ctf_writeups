# Easy Peasy

## Problem

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) `nc mercury.picoctf.net 58913` otp.py

## Solution

when we do this `nc mercury.picoctf.net 58913` we get this output:

```
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57

What data would you like to encrypt?
```

the length of the encrypted flag is 64

if we enter 50000 a's as input, using this command `python3 -c "print('a'*49968);print('a'*32)" | nc mercury.picoctf.net 58913` we get the following

```
03464b4f1a1c3a313d1951573d195102383d1907533d1905033d1904043d1904
```

using python, we could get the flag from the following logic:

1. `ef=f^k`
2. `ea=pa^k`
3. `ea^ef=f^pa`
4. `f=ea^ef^pa`

Here's the python code to get the hex value of the flag

```py
ea=0x03464b4f1a1c3a313d1951573d195102383d1907533d1905033d1904043d1904
ef=0x51124f4d194969633e4b52026f4c07513a6f4d05516e1e50536c4954066a1c57
pa=0x6161616161616161616161616161616161616161616161616161616161616161
print("{:x}".format(ea^ef^pa))
```

output: `3335656362343233623362343334373263333563633266343130313163366432`

if we convert it to ASCII, we get the flag

FLAG: `picoCTF{35ecb423b3b43472c35cc2f41011c6d2}`