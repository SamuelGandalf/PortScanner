#!/usr/bin/python3

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this is to create the socket object
socket.setdefaulttimeout(1) #this is to perform the scan within the specifid time.

host = input("[**] Enter The Host To Perform Scan: ")
#port = int(input("[**] Enter the Port To Scan: "))

def Port_Scanner(port):
	if sock.connect_ex((host, port)):
		print("[**] Port {} is closed" .format(port))
	else:
		print("[**] Port {} is opened" .format(port))

for port in range(20,80):
	Port_Scanner(port)

