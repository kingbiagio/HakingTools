#!/usr/bin/python
# 
# stealth scanner, it doesn't complete the three way handshake
# requirements scapy, termcolor
# apt-get install scapy
# pip install termcolor

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
from termcolor import *
from threading import *
import multiprocessing


if len(sys.argv) != 4:
    print (colored("<-- SYN SCANNER -->",'blue'))# just banner
    print (colored("Usage - ./syn_scan.py [Target-IP] [First Port] [Last Port]",'blue')) #just description
    sys.exit()
else:
 ip = sys.argv[1]
 start = int(sys.argv[2])
 end = int(sys.argv[3])

 for port in range(start,end):
    ans = sr1(IP(dst=ip)/TCP(dport=port),timeout=1,verbose =0)#variable created in scapy, change here for timeout&verbose
    if ans == None:
        pass
    else:
        if int(ans[TCP].flags) == 18:
            print (colored(port,'yellow'))
        else:
            pass
