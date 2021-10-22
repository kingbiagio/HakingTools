#!/usr/bin/python3

import hashlib
import pyfiglet
import sys

ascii_banner = pyfiglet.figlet_format("HASH CRACKER", font="digital")
print(ascii_banner)
print("[+] Start Cracking...")

wordlist_location = sys.argv[1]
hash_input = sys.argv[2]

with open(wordlist_location, 'r', encoding='latin-1') as file:
	for line in file.readlines():
		hash_ob = hashlib.md5(line.strip().encode())
		hashed_pass = hash_ob.hexdigest()
		if hashed_pass == hash_input:
			print("[+] Password is: " + line.strip())
			exit(0)
	else:
		print("[!] No Password Found!")
		exit(0)
