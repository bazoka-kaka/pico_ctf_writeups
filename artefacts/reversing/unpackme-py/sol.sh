#!/usr/bin/bash

python3 unpackme.flag.py | grep -oE picoCTF{.*?} --color=none
