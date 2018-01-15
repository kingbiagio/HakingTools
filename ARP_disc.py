#!/usr/bin/python
# Author Biagio
#
# It sends ARP packet to Subnet to sollicts a MAC
# requirements install scapy and termcolor libraries
# apt install scapy 
# pip install termcolor

import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
from termcolor import*  
from threading import*

if len(sys.argv) != 2:
	print (colored("<--ARP DISCOVERY-->",'blue'))# Just Banner
	print (colored("Usage - ./ARP_disc.py [interface]",'blue'))
	sys.exit()

interface = str(sys.argv[1]) # interface
ip = subprocess.check_output("ifconfig " + interface + " | grep 'inet ' |  awk '{ print $2 }' | cut -d ':' -f2", shell=True).strip() # simple grep
prefix = ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.'  

for addr in range(1,254): #change this for different Subnet, In this case is \24
	answer=sr1(ARP(pdst=prefix+str(addr)),timeout=1,verbose=0) #variable created in scapy If you need change here for Timeout & Verbose
	if answer == None: 
		pass
	else:
		print (colored(prefix+str(addr),'blue'))
