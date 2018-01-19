#!/usr/bin/python
#
# Author Biagio
# Version 1.2
#
# It sends ARP packet to Subnet to sollicts a IP response 
# requirements install scapy and termcolor libraries
# apt install scapy && pip install scapy
# pip install termcolor
#
# Usage ./ARP_disc.py [Interface]
# Example ./ARP_disc.py [eth0]  "<type ifconfig to see your Interface>"
#


import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
from termcolor import*  
from threadirtng import*
import multiprocessing

if len(sys.argv) != 2:
	print (colored("Usage - ./ARP_disc.py [Interface]",'blue'))
	sys.exit()

interface = str(sys.argv[1]) # interface
ip = subprocess.check_output("ifconfig " + interface + " | grep 'inet ' |  awk '{ print $2 }' | cut -d ':' -f2", shell=True).strip() # simple grep
prefix = ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.'  

print (colored("<--ARP SENDER-->",'blue'))

for addr in range(1,254): # Change here for different CIDR
	try: 
		answer=sr1(ARP(pdst=prefix+str(addr)),timeout=1,verbose=0) #If you need change here for Timeout & Verbose
		if answer == None: 
			pass 
		else: 
			print prefix+str(addr)
	# If User press Ctrl+c, tool will be quit
	except KeyboardIterrupt:
		print (colored("[!] Proccess Stopped"))
		sys.exit()
