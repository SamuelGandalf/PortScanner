#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "172.18.112.1"
port = 135

def Port_Scanner(port):
	if sock.connect_ex((host, port)):
		print "Port %d is closed!" %(port)
	else:
		print "Port %d is opened!" %(port)
Port_Scanner(port)
