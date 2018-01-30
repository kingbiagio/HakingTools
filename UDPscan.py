#!/usr/bin/python
# not yet Stable!!!
# some Bug are yet in place!!
# -----------------------------------------------------------
# Python 2                                                   |
# Author ScianKabestia                                       |
# Version 1.3beta                                            |
# Bug Fixes, increase speed, print Closed Port & Open Ports  |
#                                                            |
# Requirements: install termcolor "pip install termcolor"    |
#               apt-get install scapy                        |
#               install scapy "pip install scapy"            |
# Default Timeout 5 seconds                                  |
# Usage - ./UDPscan.py [IP] [First Port] [Last Port]         |
# Example - ./UDPscan.py 8.8.8.8 1 100                       |
# -----------------------------------------------------------

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
from threading import *
import multiprocessing
import sys
from termcolor import*


if len(sys.argv) != 4:
    #simle banner
    print (colored("./UDPscan.py [IP] [FirstPort] [LastPort]",'blue'))
    sys.exit()
    
else:#--global variables--#
    ip = sys.argv[1] 
    start = int(sys.argv[2]) 
    end = int(sys.argv[3])

print(colored("<--- UDP PORT SCANNER --->",'blue'))
print "Author: ScianKaBestia\n"

for port in range(start,end+1):
    try: 
        ans = sr1(IP(dst=ip)/UDP(dport=port),timeout=5,verbose =0)#change here for different Timeout&Verbose
        time.sleep(1) 
        if ans == None: 
            print port,"UDP",(colored("[OPEN]",'green'))# print open port 
        else: 
            print port,"UDP",(colored("[CLOSED]",'red'))# print closed port
            pass
    #If user press Ctrl+c
    except KeyboardInterrupt:
        print "[!] Process Stopped"
        sys.exit()

