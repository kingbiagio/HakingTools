#!/usr/bin/python
#Auhtor Biagio
#
# It Send TCP ACK Flag, will determine if port is Filtred or Not 
# if port is filtered we received a RST flag
#

from termcolor import colored
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from threading import *

if len(sys.argv) != 3:	
	print (colored("<---FIREWALL DETECTIONER--->",'yellow'))
	print (colored("Usage- ./ACK_FW.py [IP] [Port]", 'yellow'))
	sys.exit()			

ip = sys.argv[1]
port = int (sys.argv[2])

#Change here for different Timeout&Verbose
ACK_response = sr1(IP(dst= ip)/TCP(dport= port, flags='A'), timeout=1, verbose=0)
SYN_response = sr1(IP(dst= ip)/TCP(dport= port, flags='S'), timeout=1, verbose=0)

# If ACK_response and SYN_response are NONE, the Port
# is either unstatefully filtered or Host is Down
if (ACK_response == None) and (SYN_response == None) :
	print(colored("[+]Port is either Unstatefully Filtered, or Host is Down!",'red'))

#if one Response of Variable is None, Port is Filtered
elif ((ACK_response == None) or (SYN_response == None)) and not ((ACK_response == None) and (SYN_response == None)):
	print(colored("[!]Port is Filtered and Open",'red'))

elif int(SYN_response[TCP].flags) == 18:#Change different flag
	print(colored("[+]Port is Unfiltered and Open",'green'))

elif int(SYN_response[TCP].flags) == 20:#Change here for different Flag
	print(colored("[+]Port is Unfiltered and Close",'yellow'))

else:
	print(colored("[!]ERROR Unable to determine if the Port is Filtered",'red'))
