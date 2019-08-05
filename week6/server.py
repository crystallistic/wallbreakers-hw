#!/usr/bin/env python3

import socket

host, port = "127.0.0.1", 3333

# server socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(5)
    clientsocket,address = s.accept()

    # do the stuff
    with clientsocket:
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            clientsocket.sendall(data)

