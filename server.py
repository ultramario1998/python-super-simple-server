import socketserver
import socket

class handler(socketserver.BaseRequestHandler):
	def handle(self):
		# define data as whatever we receive
		self.data = self.request.recv(1024).strip()
		# "(client address) says:"
		print("{} says:".format(self.client_address[0]))
		print(self.data)
		self.request.sendall("Data received.")

def startServer(ip, port):
	print("running server on ip " + str(ip) + " and port " + str(port))
	# apparently using WITH AS makes things close much cleaner, which is fine by me
	with socketserver.TCPServer((ip, port), handler) as server:
		server.serve_forever()