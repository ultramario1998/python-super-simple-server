# Overview

This is a super simple program that sends and receives requests between two computers. Choose whether to run the client or server, supply it with the server's IP address, and type in what you'd like to send.

I wrote this mostly to gain experience with network requests.

[Software Demo Video](https://youtu.be/YhF8K0QixOg)

# Network Communication

This is a client/server based communication, with some shell code that lets the user choose which one they'd like to run.

It uses TCP, and defaults to port 9999, although the user can specify which port to use should they choose.

All messages are sent as bytes in UTF-8.

# Development Environment

I used the commandline, as well as the Socket and Socketserver libraries for python.

# Useful Websites

* [Socket](https://docs.python.org/3/library/socket.html)
* [Socketserver](https://docs.python.org/3/library/socketserver.html#socketserver.UDPServer)

# Future Work

* Make it so that the client can send multiple requests in a row
* Make it so that the client can send files
* Automatically choose local IP instead of localhost