#from socketserver import TCPServer
import socket

def attemptConnection(address):
	test = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
	test.bind(address)
	test.accept()
	hostname = socket.getfqdn()
	print(hostname)
	socket.create_connection(address,60)

address = ('127.0.0.1',80)

attemptConnection(address)