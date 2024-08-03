# Unpackme

## Problem

Can you get the flag? Reverse engineer this binary.

## Solution

we know that the file is upx compressed, we know that the file is compressed from the following command `binwalk unpackme-upx`

output:
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ELF, 64-bit LSB executable, AMD x86-64, version 1 (GNU/Linux)
272           0x110           ELF, 64-bit LSB processor-specific, (GNU/Linux)
348669        0x551FD         Copyright string: "Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $"
```

we have to uncompress it first using the command `upx -d unpackme-upx`

if we binwalk it again:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             ELF, 64-bit LSB executable, AMD x86-64, version 1 (GNU/Linux)
734000        0xB3330         Unix path: /usr/share/locale
749270        0xB6ED6         Unix path: /usr/lib/getconf
757104        0xB8D70         Unix path: /usr/lib/locale
759104        0xB9540         Unix path: /usr/lib/locale/locale-archive
839479        0xCCF37         Unix path: /usr/lib/x86_64-linux-gnu/
```

we have to make the file executable using the command `chmod +x unpackme-upx`

we use ghidra to try finding out what the program does, it seems like the program is also checking the favorite number again

from the following code part:

```c
  printf("What\'s my favorite number? ");
  __isoc99_scanf(&DAT_004b3020,&local_44);
  if (local_44 == 0xb83cb) {
    local_40 = (char *)rotate_encrypt(0,&local_38);
    fputs(local_40,(FILE *)stdout);
    putchar(10);
    free(local_40);
  }
```

we know that the favorite number is 0xb83cb which is 754635 in decimal form

FLAG: `picoCTF{up><_m3_f7w_e510a27f}`