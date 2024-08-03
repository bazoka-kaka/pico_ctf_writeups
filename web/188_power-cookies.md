# Power Cookies

## Problem

Can you get the flag?

Additional details will be available after launching your challenge instance.

## Solution

Just change the value of isAdmin cookie to 1

we could also use the following linux command `curl http://saturn.picoctf.net:65114/check.php --cookie isAdmin=1 | grep -oE picoCTF{.*?} --color=none`

FLAG: `picoCTF{gr4d3_A_c00k13_0d351e23}`