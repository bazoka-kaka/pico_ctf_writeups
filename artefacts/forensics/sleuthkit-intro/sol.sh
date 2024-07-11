#!/usr/bin/bash

echo 202752 | nc saturn.picoctf.net 51031 | grep -oE picoCTF{.*?} --color=none
