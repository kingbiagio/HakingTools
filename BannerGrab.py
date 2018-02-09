#!/usr/bin/python
#
# Author Sciankabestia
# Version 0.1beta
# Simple BannerGrabbing
# It attempts to Connect to port and
# prints version, protocol, patches
#

from threading import*
from socket import*
import socket

print "---------------------------------------"
print(colored("<-- BANNER GRABBING -->",'red'))
print "Version: 0.1beta"
print "Author: ScianKaBestia"
print "Timeout is set 20 Seconds"
print "---------------------------------------\n"

socket.setdefaulttimeout(20)# Timeout
sock = socket.socket()
Target = raw_input(colored("[+] Enter IP: ",'yellow'))
Port = int (raw_input (colored("[+] Enter PORT: ",'yellow')))
sock.connect((Target, Port))
print

print(colored (sock.recv(4096),'blue'))
sock.close()
