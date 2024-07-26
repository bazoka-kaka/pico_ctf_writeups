# Roboto Sans

## Problem

The flag is somewhere on this web application not necessarily on the website. Find it.

Additional details will be available after launching your challenge instance.

## Solution

If you go to /robots.txt

```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

if you decode using the following command: `echo anMvbXlmaWxlLnR4dA== | base64 -d`

output: js/myfile.txt

go there and you'll find the flag

FLAG: `picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}`