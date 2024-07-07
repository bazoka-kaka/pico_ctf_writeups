# Transformation

## Problem:
I wonder what this really is... ``enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])``

## Solution:

just comment out the calling function of choose_greatest() and add this line

``
decode_secret(bezos_cc_secret)
``