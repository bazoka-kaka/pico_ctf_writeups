# New Caesar

## Problem

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil new_caesar.py

## Solution

First, we have to understand the encryption code

We know that the alphabet used to encode is consisted of the first 16 lowercase alphabet letters

```py
ALPHABET = string.ascii_lowercase[:16]
```

Encryption logics:

```py
def b16_encode(plain):
        enc = ""
        for c in plain:
                # example c = 'a'
                # binary = a in 8 chars binary string
                # binary = '01100001'
                binary = "{0:08b}".format(ord(c))
                # int(binary[:4], 2) --> first 4 chars of the binary string '0110' --> convert to int = 6 --> the 6th ALPHABET is g
                # enc = 'g'
                enc += ALPHABET[int(binary[:4], 2)]
                # int(binary[4:], 2) --> last 4 chars of the binary string '0001' --> convert to int = 1 --> the 1st ALPHABET is b
                # enc = 'gb'
                enc += ALPHABET[int(binary[4:], 2)]
        return enc
```

since the following function:

```py
def shift(c, k):
        t1 = ord(c) - LOWERCASE_OFFSET
        t2 = ord(k) - LOWERCASE_OFFSET
        return ALPHABET[(t1 + t2) % len(ALPHABET)]
```

is just the same when we're doing encryption and decryption, we're not gonna bother trying to understand the logics since it's also just shifting by k characters

Here's the solution script:

```py
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

# solve code
def b16_decode(encoded):
    dec = ""
    for i in range(0, len(encoded), 2):
        a = "{0:04b}".format(ord(encoded[i]) - LOWERCASE_OFFSET)
        b = "{0:04b}".format(ord(encoded[i+1]) - LOWERCASE_OFFSET)
        dec += chr(int(a + b, 2))
    return dec

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

b16 = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

for key in ALPHABET:
    shifted = ""
    for i, c in enumerate(b16):
        shifted += shift(c, key[i % len(key)])
    flag = b16_decode(shifted)
    print(flag)

```

there are 16 possibilities but only 1 is the flag

FLAG: `picoCTF{et_tu?_431db62c5618cd75f1d0b83832b67b46}`
