#!/usr/bin/python
#
#--------------------------------------------------------------
# Python 2                                                     |
# Auhtor Biagio                                                |
# Version 1.3                                                  |
#                                                              |
# Bug fixes, increased speed, print Open & Closed Ports        |
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

# global variable ------
ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

print (colored("<--TCP SYN PORT SCANNER-->",'blue'))#banner

for port in range(start,end+1):
    try:                                   #change here different timeout&verbose
        ans = sr1(IP(dst=ip)/TCP(dport=port),timeout=5 ,verbose=0) #variable created in scapy
        time.sleep(0.4)#change here different time sleep
        if ans == None:    
            pass
        else:
            if int(ans[TCP].flags) == 18:
                print (colored(port,'green')) ,(colored("[OPEN]",'green'))#print open port 
            else: 
                pass 
            print (colored(port,'red')), (colored("[CLOSED]",'red'))#print closed port

    #If User press Ctrl+c
    except KeyboardInterrupt:
        print "[!] Process Stopped"
        sys.exit()
