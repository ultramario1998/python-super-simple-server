import socket

def startClient(ip, port):
	with socket.socket() as connection_socket:
		#connect to ip
		connection_socket.connect((ip, port))
		#if we get here, we're probably successful. we do, however, need data to send.
		#we also want to run this indefinitely until we choose to quit
		print("Connection successful.")
		send_data = str(input("Input data to send: "))
		#encode and send the data...
		connection_socket.sendall(bytes(send_data + '\n', "utf-8"))
		#and await the server's response.
		received_data = str(connection_socket.recv(1024), "utf-8")
		print("Sent:		{}\nReceived:   {}\n".format(send_data, received_data))