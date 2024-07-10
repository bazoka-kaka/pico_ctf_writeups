# Lookey Here

## Problem

Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data here.

## Solution

Here's the solution script:

```
#!/usr/bin/bash

cat anthem.flag.txt | grep -oE picoCTF{.*?} --color=none
```

Here's the flag: picoCTF{gr3p*15*@w3s0m3_2116b979}
