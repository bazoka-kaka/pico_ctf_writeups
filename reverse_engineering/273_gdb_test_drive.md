# GDB Test Drive

## Problem
Can you get the flag?

## Solution

```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

flag: picoCTF{d3bugg3r_dr1v3_197c378a}