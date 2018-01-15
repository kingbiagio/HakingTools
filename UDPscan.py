#!/usr/bin/python
#Author Biagio 
#
# install termcolor "pip install termcolor"
#

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import time
import sys
from termcolor import*


if len(sys.argv) != 4:
    print (colored("       <---UDP SCANNER--->",'blue'))#simle banner
    print (colored("./UDPscan.py [IP] [FirstPort] [LastPort]",'blue'))
    sys.exit()
    
else:
 ip = sys.argv[1]
 start = int(sys.argv[2])
 end = int(sys.argv[3])

 for port in range(start,end):
    ans = sr1(IP(dst=ip)/UDP(dport=port),timeout=5,verbose =0)#change here for different Timeout&Verbose
    time.sleep(1)
    if ans == None:
        print (colored(port ,'yellow'))
    else:
        pass
