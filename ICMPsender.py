#!/usr/bin/python
#
# Python 2
# Simple ICMP Discovery tool
# Author Mikael
# Version 1.1
# sends ICMP Packet ECHO REQUEST to subnet, it sollicits a response
# Requirements Scapy, termcolor pip install 
# 
# Usage - ./ICMPsender.py [IP/24 CIDR]
# Example - ./ICMPsender.py [192.168.0.1/24]
#

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
from termcolor import*

if len(sys.argv) != 2:
	print (colored("Usage - ./ICMPsender.py [IP/24 CIDR]\n",'red'))
	sys.exit()

#--global variable
address = str(sys.argv[1])
prefix = address.split('.')[0] + '.' + address.split('.')[1] + '.' + address.split('.')[2] + '.'

print "-------------------------------------"
print (colored("<--ICMP DISCOVERY-->",'red'))
print "Author: Mikael"
print "Version: 1.1"
print "-------------------------------------\n"

for addr in range(1,254): 
	try: 
		answer=sr1(IP(dst=prefix+str(addr))/ICMP(),timeout=1 , verbose=0)#Change here for different Timeout 
		if answer == None: 
			pass 
		else: 
			print (colored(prefix+str(addr),'red')) 
	#When User Press Ctrl+c,tool will be Closed 
	except KeyboardInterrupt:
		print "[!] Proccess Stopped "
                sys.exit()
