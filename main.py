#!/usr/bin/python3

import socket

host = "127.0.0.1"
port = 5321

clients = []

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto = 0)
serv_sock.bind((host, port))
serv_sock.listen(10)

quit = False

print("***Server started!")

while True:

    client_sock, client_addr = serv_sock.accept()
    print(client_addr)

    while True:

        data = client_sock.recv(1024)
        if not data:
            break
        client_sock.sendall(data)


serv_sock.close()
