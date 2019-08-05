#!/usr/bin/env python3
 
import socket, select, os, sys

host, port = 'localhost', 59999

serversocket = socket.socket()
serversocket.bind((host,port))
serversocket.listen(10)

print(f"Serving HTTP on port {port}...")

for i in range(5):
    
    n = os.fork()
    if n == 0:
        
        pid  = os.getpid()
        print("Child", pid, "accepting on shared socket (localhost:60003)")
        try:
            while 1:
                clientconnection, clientaddress = serversocket.accept()
                b = clientconnection.makefile("rw")
                b.write('Child' + str(pid) + "echo")
                message = b.read()
                b.write(message)
                b.close()

                print("Child %s echoed: %r" % (pid, message.strip()))
        except KeyboardInterrupt:
            sys.exit()
try:
    os.waitpid(-1,0)
except KeyboardInterrupt:
    print("exit")
    sys.exit()

serversocket.close()