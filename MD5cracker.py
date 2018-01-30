#!/usr/bin/python2.7
#
# Author ScianKaBestia
# Version 1.2
# Python 2
# Simple Hash md5 Cracker, run it with python 2.7
# requirements termcolor
#

from threading import*
import multiprocessing
import sys
import os
import socket
import md5
from termcolor import*
import time

print (colored("\n<<<< MD5 CRACKER >>>",'yellow')) # just banner
print "Author: ScianKaBestia\n"
counter=1
user= raw_input(colored("[+] Insert User's hash You wish to Crack (or Press Enter to Skip): ",'yellow'))#Banner
pass_in= raw_input (colored("[+] Insert User's MD5 hash: ",'yellow'))
pwfile= raw_input (colored("[+] Insert your path file name: ",'yellow'))

print (colored("[*] Have Good Cracking ;)\n",'blue'))
time.sleep(0.4) #Timeout, change here different Timeout

try:
	pwfile= open(pwfile, "r")
except:
	print (colored("\n[!] File Not Found, Plese try again.",'red'))# banner
	quit()


for password in pwfile:
	filemd5= md5.new(password.strip()).hexdigest() 
	print (colored("Trying password number: %d: %s",'red')) % (counter, password.strip())

	counter+=1

	if pass_in== filemd5:
		print(colored("Password is: %s" % password,'green')) 
		print (colored("For User: %s" % user ,'green'))
		break

else: print (colored("\nPassword Not Found for User: %s"% user,'red'))
