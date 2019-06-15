#!/usr/bin/python
#
#--------------------------------------------------------------
# Python 2                                                     |
# Auhtor: Mikael                                               |
# Version: 1.4                                                 |
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
# Usage - ./TCPsynScan.py [IP/HOSTNAME] [First Port] [Last Port]        |
# Example - ./TCPsynScan.py 8.8.8.8 1 80                       |
#--------------------------------------------------------------


import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
from termcolor import *
import time

if len(sys.argv) != 4:
    print (colored("Usage - ./TCPsynScan.py [IP/HOSTNAME] [First Port] [Last Port]",'blue')) #just description
    sys.exit()

else: 
    ip = sys.argv[1] 
    start = int(sys.argv[2]) 
    end = int(sys.argv[3])
    version = 1.4
    Author = "Mikael"

# Banner
print "----------------------------------------"
print (colored("<--TCP SYN PORT SCANNER-->",'blue'))
print "Version:",version
print "Author:" ,Author
print "IP/HOSTNAME:" ,ip
print "----------------------------------------\n"

for port in range(start,end+1):
    try:                                  #Set Timeout   #Set Verbose
        ans = sr1(IP(dst=ip)/TCP(dport=port),timeout=1 ,verbose =0) #variable created in scapy
        time.sleep(0.2)# Comment for more Speed
        if ans == None: 
            print port,"TCP", (colored("[NO RESPONSE RETURNED, PORT FILTERED/HOST DOWN]",'red'))# port is either Filtered or Closed
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
