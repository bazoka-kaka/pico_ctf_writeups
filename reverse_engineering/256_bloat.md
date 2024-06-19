# Bloat

## Problem

Can you get the flag? Run this Python program in the same directory as this encrypted flag.

## Solution

we have to decode the strings, for example:

```
print(a[54]+a[68]+a[75]+a[66]+a[78]+a[76]+a[68]+a[94]+a[65]+a[64]+a[66]+\
a[74]+a[13]+a[13]+a[13]+a[94]+a[88]+a[78]+a[84]+a[81]+a[94]+a[69]+\
a[75]+a[64]+a[70]+a[11]+a[94]+a[84]+a[82]+a[68]+a[81]+a[25])
```

do this for a lot of them then also change the function names, it'll become something like this

```
import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def check_pass(arg432):
  if arg432 == "happychance":
    return True
  else:
    print("That password is incorrect")
    sys.exit(0)
    return False
def decode_fun(arg444):
  return arg122(arg444.decode(), "rapscallion")
def enter_pass():
  return input("Please enter correct password for flag:")
def read_flag():
  return open('flag.txt.enc', 'rb').read()
def arg112():
  print("Welcome back... your flag, user:")
def arg122(arg432, arg423):
    arg433 = arg423
    i = 0
    while len(arg433) < len(arg432):
        arg433 = arg433 + arg423[i]
        i = (i + 1) % len(arg423)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(arg432,arg433)])
arg444 = read_flag()
arg432 = enter_pass()
check_pass(arg432)
arg112()
arg423 = decode_fun(arg444)
print(arg423)
sys.exit(0)
```

then if you see the function "check_pass" above, we'll see the password when you run the program is "rapscallion"

the flag: picoCTF{d30bfu5c4710n_f7w_b8062eec}