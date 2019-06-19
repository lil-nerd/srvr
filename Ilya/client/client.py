#!/usr/bin/python3
import socket
import threading

from help import *
from face import Chat_window
class Client():

	client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	name = "default"

	def send_msg(self):
		while True:
			self.client_sock.send(to_data(input("")))
			print("***msg sent")


	def __init__(self):

		print("Client is working!!!")

		host = "127.0.0.1"
		port = 5231
		self.server = (host, port)

		self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_sock.connect(self.server)
		print("You have been connected to " + str(host))

		self.name = input("Enter your nickname: ")
		self.client_sock.send(to_data(self.name))

#		cl_thread = threading.Thread(target = self.send_msg)
#		cl_thread.deamon = True
#		cl_thread.start()



	def run_client(self):

		window = Chat_window(self.name)

		while True:
			data = self.client_sock.recv(1024)
			if not data:
				print("bye")
				break
			print(get_data(data))
