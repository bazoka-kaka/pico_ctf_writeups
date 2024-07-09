# Credstuff

## Problem

We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it? Download the leak here. The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.

## Solution

The username is found in the nth line of the file usernames.txt, find the password in the same line in the file passwords.txt. We know that the password is encrypted using ROT13 caesar encryption.

we can use bash script to decrypt the password:

```
echo "cvpbPGS{P7e1S_54I35_71Z3}" | tr "A-Za-z" "N-ZA-Mn-za-m"
```

another way: we could do `sudo apt install bsdgames -y` then solve using the command `echo "cvpbPGS{P7e1S_54I35_71Z3}" | rot13`

flag: picoCTF{C7r1F_54V35_71M3}
