# File Run 2

## Problem
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?

## Solution

```
$ chmod +x run.1
$ ./run.1 "Hello!" | grep -oE "picoCTF{.*}" --color=none
```

flag: picoCTF{F1r57_4rgum3n7_96f2195f}