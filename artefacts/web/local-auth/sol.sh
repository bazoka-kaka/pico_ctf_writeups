#!/usr/bin/bash

curl -X POST --data hash=2196812e91c29df34f5e217cfd639881 "http://saturn.picoctf.net:64275/admin.php" | grep -oE picoCTF{.*?} --color=none