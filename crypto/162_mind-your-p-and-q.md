# Mind Your Ps and Qs

## Problem

In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values

## Solution

use dcode.fr then enter the following values

c: 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n: 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e: 65537

another method is to use the following tool https://github.com/RsaCtfTool/RsaCtfTool

installation: 

```sh
$ git clone https://github.com/RsaCtfTool/RsaCtfTool
# create new python environment
$ python3 -m venv .venv
# activate python environment
$ source . .venv/bin/activate
# install requirements
$ pip install -r requirements.txt
```

run the tool with the following command: `python3 RsaCtfTool.py -n 1422450808944701344261903748621562998784243662042303391362692043823716783771691667 -e 65537 --decrypt 843044897663847841476319711639772861390329326681532977209935413827620909782846667`

FLAG: `picoCTF{sma11_N_n0_g0od_00264570}`