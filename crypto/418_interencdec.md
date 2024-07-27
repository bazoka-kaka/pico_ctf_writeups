# interencdec

## Problem

Can you get the real meaning from this file.

## Solution

wget the following base64 encrypted string `YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==`

we then have to decrypt it twice

1st iteration: `cat enc_flag | base64 -d` output: `d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ==`

2nd iteration: `echo d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzg5MGsyMzc5fQ== | base64 -d` output: `wpjvJAM{jhlzhy_k3jy9wa3k_890k2379}`

decrypt it using ROT

FLAG: `	picoCTF{caesar_d3cr9pt3d_890d2379}`