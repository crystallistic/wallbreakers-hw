#!/usr/bin/env python3
import socket

host, port = "127.0.0.1", 3333
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b'HI bish')
    data = s.recv(1024)

print("Received", repr(data))
