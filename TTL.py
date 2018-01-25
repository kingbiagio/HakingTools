#!/usr/bin/python2.7
#
# Author SciancaBestia
# Python 2
# Version 1.1
# Requirements colored "pip install termcolor"
#
# It analyzes TTL value, to determinate if Os 
# is Microsoft/windows or Linux/unix & CiscoRouterNetwork 
#
#  -------------------------------
# |  CiscoRouterNetwork: 255 ttl  |
# |  Microsoft/Windows:  128 ttl  |
# |  Unix/Like:           64 ttl  |
#  ------------------------------- 
# Usage ./TTL.py 8.8.8.8
# Example ./TTL.py 8.8.8.8
#


import multiprocessing
from threading import *
from scapy.all import *
import logging
from termcolor import *
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

if len(sys.argv) != 2:
        #just banner
	print "Usage - ./TTL.py [Target IP]"
	sys.exit()

ip = sys.argv[1]              
ans= sr1(IP(dst=str(ip))/ICMP(), timeout=5, verbose=0)# Scapy variable set to [ICMP] protocol,
                                                      # Change here for different Timeout&Verbose
	                         
print (colored("<--TTL ANALYZER-->",'yellow'))
if ans== None: # if none response was returned there is a Firewall behind or Host is Down
	print(colored("[!] No response was returned Firewall blocks [ICMP] or Host is Down",'red'))

elif int (ans[IP].ttl) >=254:# if OS is CiscoRouterNetwork
        print(colored("[+] Host is Cisco Router Network",'blue'))

elif int (ans[IP].ttl) <= 64:#If OS Unix/linux
	print (colored("[+] Host is Linux/Unix Os",'yellow'))

else:                      #if OS is Windows
	print(colored("[+] Host is Microsoft/Windows",'blue'))
