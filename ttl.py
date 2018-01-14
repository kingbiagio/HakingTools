#!/usr/bin/python
#
#Python version2
#
# it analyze TTL value, to determinate if Os 
# is Microsoft/windows or Unix
#
# Microsoft/Windows:  128 ttl
# Unix/Like:           64 ttl
# 

from threading import *
from scapy.all import *
import logging
from termcolor import *
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

if len(sys.argv) != 2:
	print(colored("<TTL ANALYZER>",'blue'))
	print "Usage - ./ttl.py [Target]"
	print "Usage - ./ttl.py 8.8.8.8."
	sys.exit()

ip = sys.argv[1]
ans= sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
if ans== None:
	print(colored("[!] No response was returned Firewall blocks [ICMP] or Host is Down",'red'))

elif int (ans[IP].ttl) >=254:
        print(colored("[+] Host is Cisco Router Network",'white'))

elif int (ans[IP].ttl) <= 64:
	print (colored("[+] Host is Linux/Unix Os",'yellow'))

else:
	print(colored("[+] Host is Microsoft/Windows",'blue'))
