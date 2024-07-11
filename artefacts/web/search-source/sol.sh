#!/usr/bin/bash

grep -RoE picoCTF{.*?} | cut -d ":" -f3
