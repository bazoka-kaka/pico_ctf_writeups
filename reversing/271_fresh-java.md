# Fresh Java

## Problem

Can you get the flag? Reverse engineer this Java program.

## Solution

use JADX to convert .class file to .java file

after trimming stuffs you get this

```
}
d
0
a
1
e
f
b
2
_
d
3
r
1
u
q
3
r
_
g
n
1
l
0
0
7
{
F
T
C
o
c
i
p
```

to reverse and remove the space, use the following bash script

```sh
#!/usr/bin/bash

cat flag.txt | tac | tr -d "\n"
```

FLAG: `picoCTF{700l1ng_r3qu1r3d_2bfe1a0d}`