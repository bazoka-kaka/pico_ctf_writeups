# bbbloat

## Problem

Can you get the flag? Reverse engineer this binary.

## Solution

Before using stuffs like IDA pro or Ghidra or any other debugger run these some command utilities tool:
- strace
- ltrace

They're kinda like debugger but not, instead they see how things run and operate alongside the binary without stopping, without break points

but they'll list out any library calls that it made from like c center library

for more info: `$ man strace` `$ man ltrace`

note: ltrace = library trace, strace = signal trace

another tool: `$ objdump -d [filename]`

just use ghidra --> windows tab --> defined strings --> find "Whats my fav number" --> go there --> go to the function --> see the disassembled c --> you'll get 0x86187 --> python3 -->

```
a = 0x86187
0x86187
```

output flag: picoCTF{cu7_7h3_bl047_695036e3}