#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #this is to create the socket object
socket.setdefaulttimeout(15) #this is to perform the scan within the specified time.

host = input("[**] Enter The Host To Perform Scan: ")
#port = int(nput("[**] Enter the Port To Scan: "))

def Port_Scanner(port):
	if sock.connect_ex((host, port)):
		print(colored("Port %d is closed!" %(port), 'red'))
	else:
		print(colored("Port %d is opened!" %(port), 'green'))
for port in range(1, 100): #range of the ports to be scanned
	Port_Scanner(port)
