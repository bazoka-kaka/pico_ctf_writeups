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
