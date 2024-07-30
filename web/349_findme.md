# Findme

## Problem

Help us test the form by submiting the username as test and password as test!

Additional details will be available after launching your challenge instance.

## Solution

in http://saturn.picoctf.net:54654/ when we try to enter user: test and pass: test, we get the following output: `try username:test and password:test!`

when we go back to the earlier page and try user: test and pass: test!, we're redirected to the following pages in sequence `/next-page/id=cGljb0NURntwcm94aWVzX2Fs` `/next-page/id=bF90aGVfd2F5X2EwZmUwNzRmfQ==` `/home`

There's something odd in the /next-page where we can see 2 ids each are base64 encoded string, when we try to decoded them, we get 2 parts of the flag.

FLAG: `picoCTF{proxies_all_the_way_a0fe074f}`