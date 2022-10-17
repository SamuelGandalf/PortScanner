#!/usr/bin/python

from socket import *
import optparse  #this library has functons that allows to specify the help options to be prompted to the user
from optparse import OptionParser
from threading import *

def Connection_Scan(target_host, target_port):
	try:
		sock = socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((target_host, target_port))
		print("[**] %d/tcp Open " %(target_port))
	except:
		print("[**] %d/tcp Closed " %(target_port))

def Scan_Port(target_host, target_ports):
	try:
		target_IP = gethostbyname(target_host)  #the gethostname() function resolves the domain name into the IP address
	except:
		print("Unknown host %s" %(target_host))
	try:
		target_Name = gethostbyaddr(target_IP)
		print("[**] Scan results for: " +  target_name[0])
	except:
		print("[**] Scan results for: " +  target_IP)
	setdefaulttimeout(1)
	for target_port in target_ports:
		t = Thread(target = Connection_Scan, args=(target_host, int(target_port)))
		t.start()

def main():
	parser = OptionParser("\t<---- Usage Of The Program ---->\n   -H <target host>  -p <target port>") #this is just to set the usage of the programme
	parser.add_option("-H", dest="target_host", type="string", help="Specify the target host")
	parser.add_option("-p", dest="target_port", type="string", help="Specify the target port separated by commas")
	(options, args) = parser.parse_args()
	
	target_host = options.target_host
	target_ports = str(options.target_port).split(',') #this is to separate the ports that will be entered by the ,
	
	if (target_host == None) | (target_ports[0]==None): #this is just to check and make sure the programme does not crash just incase the user does no not specify any host or port by returning the usgae of the programme
		print(parser.usage)
		exit(0)
	Scan_Port(target_host, target_ports)
if __name__ == "__main__":
	main()
#main things to keep note of are the libraries
#the optparse library contain the functions that is used to set the usage of the programme(now the sentax)
#the threading library is for 'recursiveness', used to set the thread to keep scanning the ports
#the socket library is for setting the socket object and connecting to it.


