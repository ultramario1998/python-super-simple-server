import socket

def startClient():
	listener = socket.socket()
	print('asdf')
	listener.bind((socket.gethostbyname(socket.getfqdn())))