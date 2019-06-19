
import socket
import threading

from help import *
from srvr_help import *

class Server():

    def __init__(self):
            host = "127.0.0.1"
            port = 5231
            self.server = (host, port)

            self.clients = []
            #self.cl_nicks = []

            self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto = 0)
            self.serv_sock.bind(self.server)
            self.serv_sock.listen(10)

            print("***Server is started!")


    def conn_handler(self, client, address):
        while True:
            data = client.recv(1024)
            for connection in self.clients:
                if connection == client:
                    pass
                else:
                    connection.send(data)
            if not data:
                break



    def run_Server(self):

            while True:

                client_sock, client_addr = self.serv_sock.accept()

                #THREADS
                conn_Thread = threading.Thread(target = self.conn_handler, args = (client_sock, client_addr))
                conn_Thread.deamon = True
                conn_Thread.start()

		        #Say_Hi
                #nickname = say_hello(client_sock)
                self.clients.append(client_sock)
                #self.cl_nicks.append(nickname)






#serv_sock.close()
#print_clients(clients, cl_nicks)
#print("***Server is closed!")
