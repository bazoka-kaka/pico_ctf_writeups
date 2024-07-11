# Search Source

## Problem

The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is here

## Solution

just search for the style.css, open it then get your flag

here's the flag: picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}

another technique:

download the entire website `wget -m http://saturn.picoctf.net:53957/#yoga`

then search for the entire files for the string `grep -RoE picoCTF{.*?} | cut -d ":" -f2`
