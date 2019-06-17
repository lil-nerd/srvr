#!/usr/bin/python3
import socket


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 5321))

myname = input("Your nick: ")

client_sock.sendall(b'm')


client_sock.close()
