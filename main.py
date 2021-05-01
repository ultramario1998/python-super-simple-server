

selection = input("Press 1 to send a request, or 2 to receive. ")
if selection == '1':
	print("asdf")
	ip = input("Please input the desired IP address, or leave blank to attempt localhost: ")
	if not ip:
		ip = '127.0.0.1'
	port = input("Please input the desired port, or leave blank to attempt port 80: ")
	if not port:
		port = '80'
	address = (ip,port)