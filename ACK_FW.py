#!/usr/bin/python
#
# Python 2
# Auhtor Mikael
# Version 1.2
# It Send TCP ACK Flag, will determine if port is Filtred or Not 
# if port is filtered we received a RST flag
# Requirements termcolor "pip install termcolor"
# 
# Usage - ./ACK_FW [IP/HOSTNAME] [Port]
#

from termcolor import*
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 3:	
	print (colored("Usage- ./ACK_FW.py [IP/HOSTNAME] [Port]", 'yellow'))
	sys.exit()			

ip = sys.argv[1]
port = int (sys.argv[2])
Author = "Mikael"
Version = 1.2

#Change here for different Timeout&Verbose
ACK_response = sr1(IP(dst= ip)/TCP(dport= port, flags='A'), timeout=1, verbose=0)
SYN_response = sr1(IP(dst= ip)/TCP(dport= port, flags='S'), timeout=1, verbose=0)

print "--------------------------------------------"
print (colored("<--FIREWALL DETECTION-->",'red'))
print "Version",Version
print "Author",Author
print "IP/HOSTNAME:" ,ip
print "-------------------------------------------\n"

# If ACK_response and SYN_response are NONE, the Port
# is either unstatefully filtered or Host is Down
try: 
    if (ACK_response == None) and (SYN_response == None): 
        print(colored("[+]PORT IS EITHER UNSTATEFULLY FILTERED, OR HOST IS DOWN",'red')),[port]
        
        # if one Response of Variable is None, Port is Filtered 
    elif ((ACK_response == None) or (SYN_response == None)) and not ((ACK_response == None) and (SYN_response == None)): 
        print(colored("[!]PORT IS FILTERED & OPEN",'red')),[port] 
    
    elif int(SYN_response[TCP].flags) == 18:#Change different flag value 
       print(colored("[+]PORT IS UNFILTERED & OPEN",'green')),[port]

    elif int(SYN_response[TCP].flags) == 20:#Change here for different Flag value 
        print(colored("[+]PORT IS UNFILTERED & CLOSED",'yellow')),[port] 
    else: 
        print(colored("[!]ERROR COULDN'T DETERMINE IF PORT IS FILTERED OR NOT",'red')), [port]
except KeyboardInterrupt:
    print "[*] Proccess Stopped"
    sys.exit()
