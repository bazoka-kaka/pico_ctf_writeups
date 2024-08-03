# Eavesdrop

## Problem

Download this packet capture and find the flag.

## Solution

use wireshark to analyze the pcap file

if we follow the tcp communication, we could see this conversation

```
Hey, how do you decrypt this file again?
You're serious?
Yeah, I'm serious
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Ok, great, thanks.
Let's use Discord next time, it's more secure.
C'mon, no one knows we use this program like this!
Whatever.
Hey.
Yeah?
Could you transfer the file to me again?
Oh great. Ok, over 9002?
Yeah, listening.
Sent it
Got it.
You're unbelievable
```

from the above comms, we know that the command to decrypt the uploaded file is `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`

if we follow the tcp stream of packet with id 57, we could see the following 

```
Salted__<K&....,J.......o..%....I{97X...........
```

if the fils is shown as raw instead of ASCII:

```
53616c7465645f5f3c4b26e8b8f91e2c4af8031cfaf5f8f16fd40c25d40314e6497b39375808aba186f48da42eefa895
```

we could then save as the followed tcp stream file with the file name of file.des3 then decrypt using the earlier command we get

FLAG: `picoCTF{nc_73115_411_0ee7267a}`