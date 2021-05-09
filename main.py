from server import startServer
from client import startClient

selection = input("Press 1 to start the server, or 2 to start the client. ")
if selection == '1':
	ip = input("Please input the desired IP address, or leave blank to attempt localhost: ")
	if not ip:
		ip = '127.0.0.1'
	port = input("Please input the desired port, or leave blank to attempt port 9999: ")
	if not port:
		port = 9999
	else:
		port = int(port)
	if not isinstance(port, int):
		print("Invalid port!")
	startServer(ip, port)
elif selection == '2':
	startClient()
else:
	print("Invalid selection!")