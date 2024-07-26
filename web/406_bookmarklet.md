# Bookmarklet

## Problem

Why search for the flag when I can make a bookmarklet to print it for me? Browse here, and find the flag!

## Solution

copy this:

```js
        javascript:(function() {
            var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓ¨ÍÕÄ¦í";
            var key = "picoctf";
            var decryptedFlag = "";
            for (var i = 0; i < encryptedFlag.length; i++) {
                decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
            }
            alert(decryptedFlag);
        })();
```

to the browser console and you'll get the flag

FLAG: `picoCTF{p@g3_turn3r_18d2fa20}`