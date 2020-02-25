#!/usr/bin/python
#
# Author Mikael
# Versione 1.2
#

from scapy.all import *
import logging
from termcolor import *
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import subprocess

# subprocess.call('clear', shell=True)

print ""
print (colored("      -------------------------------------- ", 'red'))
print (colored("      |< [ICMP_ECHO-REQUEST] TTL_ANALYZER >| ", 'red'))
print (colored("      |              V 1.2                 | ", 'red'))
print (colored("      |          Author: Mikael            | ", 'red'))
print (colored("      -------------------------------------- ", 'red'))

if len(sys.argv) != 2:
	print 
	print (colored("Usage:", 'yellow'))
	print (colored("        ./TTL_ANALYZER_V1.2.py [IP/HOSTNAME]", 'yellow'))
	print ""
	print (colored("Example:", 'yellow'))
	print (colored("        ./TTL_ANALYZER_V1.2 8.8.8.8 OR ./TTL_ANALYZER_V1.2 google-public-dns-a.google.com", 'yellow'))
	print 
	sys.exit()

ip  = sys.argv[1]
ans = sr1(IP(dst=str(ip))/ICMP(), timeout = 5, verbose= 0)

if ans == None:
	print
	print "[!] NO REPSONSE WAS RETURNED FROM HOST"
	print""
	print "[+] HOST IS DOWN OR FIREWALL BLOCKS [ICMP_ECHO-REQUEST]"
	print "[+] [IP/HOSTNAME]:",ip
	print

elif int (ans[IP].ttl) == 255:
	print
	print "[+] HOST SEEMS: Aix V3.2-4.1 | BSD V3.1-4.1 | HP-Ux V10.2-11 | FreeBSD V3.4/4.0"
	print "                NetBSD | OpenBSD V2.6/2.7 | OpenVMS | Solaris V2.5.1-2.6-2.7,2.8"
	print "                Stratus_OS V.TCP_OS | Sun_OS V5.7 | Ultrix V4.2-4.5 | Irix V6.5.3/6.5.8"
	print "                Linux_Kernel V2.2.14/2.4"
	print
	print "[+] [ICMP_ECHO-REPLY] TTL_VALUE = 255"
	print "[+] [IP/HOSTNAME]:",                ip
	print 

elif int (ans[IP].ttl) == 254 :
	print
	print "[+] HOST SEEMS: Cisco_OS "
	print
	print "[+] [ICMP_ECHO-REPLY] TTL_VALUE = 254"
	print "[+] [IP/HOSTNAME]:",                ip
	print

elif int (ans[IP].ttl) == 200:
	print
	print "[+] HOST SEEMS: MPE/IX (HP)"
	print
	print "[+] [ICMP_ECHO-REPLY] TTL_VALUE = 200"
	print "[+] [IP/HOSTNAME]:",                ip
	print

elif int (ans[IP].ttl) == 128:
	print
	print "[+] HOST SEEMS: Windows 98-98_SE | Windows NT 4 | Windows ME | Windows 2000 pro"
	print "                Windows 2000 Family | < Windows Server Family > 2003/2003_R2"
	print "                                                                2008/2008_R2"
	print "                                                                2012/2012_R2"
	print "                                                                2016/2019"
	print "                Windows_Os Desktop XP/Vista/7/10"
	print
	print "[+] [ICMP_ECHO-REPLY] TTL_VALUE = 128"
	print "[+] [IP/HOSTNAME]:",                ip
	print

elif int (ans[IP].ttl) == 64:
	print
	print "[+] HOST SEEMS: Compa V_Tru64/5.0 | Foundry_OS | FreeBSD V5 | Juniper_Os | Linux_Kernel V2.0.x"
	print "                Linux_Red Hat V9 | Mac_OS X Family Desktop & Server | Netgear Os | OS/2"
	print ""
	print "[+] [ICMP_ECHO-REPLY] TTL_VALUE = 64"
	print "[+] [IP/HOSTNAME]:",                ip
	print

else:
	print
	print "[?] UNKNOWN HOST"
	print ""
	print (colored("[?] [ICMP_ECHO-REPLY] TTL_VALUE =",'yellow')), int (ans[IP].ttl) # print TTL_Value
	print "[+] [IP/HOSTNAME]:",                           ip
	print 
