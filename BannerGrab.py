#!/usr/bin/python2
# Python 2.7.x
#
# Author 
# Version 0.1beta
# Simple BannerGrabbing
# It attempts to Connect to port and prints version, protocol, patches
#

from termcolor import*
from socket import*
import socket

print "---------------------------------------"
print(colored("<-- BANNER GRABBING -->",'red'))
print "Version: 0.2beta"
print "Author: Mikael & h3kd3w"
print "Timeout is set 20 Seconds"
print "---------------------------------------\n"

socket.setdefaulttimeout(20)# Timeout
conn = socket.socket()
target = raw_input(colored("[+] Enter IP: ", 'yellow'))
port = int (raw_input (colored("[+] Enter PORT: ", 'yellow')))
conn.connect((target, port))
conn.send(b'GET /\n\n')
print

print(colored (conn.recv(4096), 'blue'))
conn.close()
