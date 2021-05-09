from server import startServer
from client import startClient
import socket
import netifaces

def main():
	print(netifaces.interfaces())
	selection = input("Press 1 to start the server, or 2 to start the client. ")
	if selection != '1' and selection != '2':
		print("Invalid selection!")
		return
	ip = input("Please input the desired IP address, or leave blank to attempt local ip: ")
	if not ip:
		ip = str(socket.gethostbyname(socket.getfqdn()))
	port = input("Please input the desired port, or leave blank to attempt port 9999: ")
	if not port:
		port = 9999
	else:
		port = int(port)
	if not isinstance(port, int):
		print("Invalid port!")
	if selection == '1':
		startServer(ip, port)
	elif selection == '2':
		startClient(ip, port)
		return
	else:
		print("Invalid selection!")

main()