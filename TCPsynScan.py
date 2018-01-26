#!/usr/bin/python
#
#--------------------------------------------------------------
# Python 2                                                     |
# Auhtor Biagio                                                |
# Version 1.4                                                  |
#                                                              |
# Bug fixes, increased speed, print Open & Closed Ports        |
#                                         Filtered Ports       |
# stealth scanner, it doesn't complete the three way handshake |
#                                                              |
# requirements scapy, termcolor                                |
# apt-get install scapy                                        |
# pip install termcolor                                        | 
# default Timeout 5 seconds                                    | 
#                                                              |
# Usage - ./TCPsynScan.py [IP] [First Port] [Last Port]        |
# Example - ./TCPsynScan.py 8.8.8.8 1 80                       |
#--------------------------------------------------------------


import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
from termcolor import *
from threading import *
import multiprocessing
import time

if len(sys.argv) != 4:
    print (colored("Usage - ./TCPsynScan.py [Target-IP] [First Port] [Last Port]",'blue')) #just description
    sys.exit()

else: 
    ip = sys.argv[1] 
    start = int(sys.argv[2]) 
    end = int(sys.argv[3])
    version = 1.4
    Author = "SciankaBestia"

print (colored("<--TCP SYN PORT SCANNER-->",'blue'))#banner
print "Version:",version
print "Author:" ,Author ,"\n"


for port in range(start,end+1):
    try:
        ans = sr1(IP(dst=ip)/TCP(dport=port),timeout=1 ,verbose =0) #variable created in scapy, change here for timeout&verbose
        time.sleep(0.2)
        if ans == None: 
            print port,"TCP", (colored("[NO RESPONSE RETURNED, PORT FILTERED]",'red'))# port is either Filtered or Closed
            pass
        else:
            if int(ans[TCP].flags) == 18:
                print (colored(port,'green')) ,(colored("TCP [OPEN]",'green'))#print Open port 
            else:
                pass
                print port, "TCP" " [CLOSED]"#print Closed port


    #If User press Ctrl+c
    except KeyboardInterrupt:
        print "[!] Process Stopped"
        sys.exit()
