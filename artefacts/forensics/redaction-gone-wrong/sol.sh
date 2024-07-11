#!/usr/bin/bash

cat text.txt | grep -oE picoCTF{.*?} --color=none
