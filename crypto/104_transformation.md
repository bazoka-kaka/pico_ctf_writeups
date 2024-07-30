# Transformation

## Problem

I wonder what this really is... enc `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

encoded: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽

## Solution

Create the following python script

```py
#!/usr/bin/env python3

f = open("enc")

encoded = f.read()

decoded = []

for x in encoded:
    d1 = chr(ord(x) >> 8)
    d2 = chr(x.encode('utf-16be')[-1])
    decoded.append(d1)
    decoded.append(d2)

print("".join(decoded))

f.close()
```

FLAG: `picoCTF{16_bits_inst34d_of_8_e141a0f7}`