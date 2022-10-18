#!/usr/bin/python3

import sys
from socket import *
from datetime import datetime
from termcolor import colored
from colorama import Fore

if len(sys.argv)==2:
	target_IP = gethostbyname(sys.argv[1]) #this simply resolves the domain name into ip
else:
	print("[**] Program Usage: PortScanner2.py <IP>")
	sys.exit(0)

	
print("-" * 50)
print("<< Scanning the target >> " + str(datetime.now()))
print("-" * 50)

try:
	for Port in range(20,90):
		sock = socket(AF_INET, SOCK_STREAM)
		#socket.setdefaulttimeout(1)
		Connection = sock.connect_ex((target_IP, Port))
		if Connection == 0:
			print(Fore.GREEN + "[++] Port {} is open" .format(Port))
		else: 
			print(Fore.RED + "[**] Port {} is closed" .format(Port))
except KeyboardInterrupt:
	Print("Exiting Program")
	sys.exit(0)
#except socket.gaierror:
#	print("Host name could not be resolved")
#except socket:
#	print("Could not connect to server")
