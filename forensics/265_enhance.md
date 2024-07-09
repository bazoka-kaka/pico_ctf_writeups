# Enhance

## Problem

Download this image file and find the flag.

    Download image file

## Solution

tools we could use to investigate:

- exiftool -- look at exifdata or metadata of the program
- strings -- displays printable form of a file

we could see that in the end, there's a flag but we should do something about it

here's the script to solve the challenge:

```
#!/usr/bin/bash

cat drawing.flag.svg  | grep "</tspan" | cut -d ">" -f2 | cut -d "<" -f1 | tr -d "\n" | tr -d " "
```

here's the flag: picoCTF{3nh4nc3d_24374675}
