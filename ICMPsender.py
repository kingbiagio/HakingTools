#!/usr/bin/python
# Simple ICMP Discovery tool
# Author Biagio
# sends ICMP Packet ECHO REQUEST to subnet, it sollicits a response
# Requirements Scapy, termcolor pip install 
# 

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
from threading import*
from termcolor import*

if len(sys.argv) != 2:
	print (colored("<--[ICMP DISCOVERY--]>",'red'))#Just banner
	print (colored("Usage - ./ICMPsender.py [IP/24 network address]\n",'red'))
	sys.exit()

address = str(sys.argv[1])
prefix = address.split('.')[0] + '.' + address.split('.')[1] + '.' + address.split('.')[2] + '.'

for addr in range(1,254):  ## edit this for different Subnet in this example is \24
	answer=sr1(IP(dst=prefix+str(addr))/ICMP(),timeout=1 , verbose=0)#Change here for different Timeout
	if answer == None:
		pass
	else:
		print (colored(prefix+str(addr),'red'))
