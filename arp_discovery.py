#!/usr/bin/python3
# sudo apt install python3-scapy

from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *


print("<--- Python ARP Discovery --->")
print("")
print("USE - ./arp_discovery.py interface IP/CIDR")
print("EX - ./arp_discovery.py eth1 192.168.0.0/24")
print("")

interface = sys.argv[1]
ip_range = sys.argv[2]
broadcastMac = "ff:ff:ff:ff:ff:ff"

print("[+] Sending ARP packets..")
print("")
packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range) 

ans, unans = srp(packet, timeout =5, iface=interface, inter=0.1, verbose=False)

for send,receive in ans:
        print (receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
