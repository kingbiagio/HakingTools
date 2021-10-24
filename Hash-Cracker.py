#!/usr/bin/python3
# sudo"apt install python3-pyfiglet

import hashlib
import pyfiglet
import sys

ascii_banner = pyfiglet.figlet_format("HASH CRACKER", font="digital")
print(ascii_banner)
print("Hash Supported: MD5, SHA256\n")
print("USE - ./Hash-Cracker.py [WORDLIST-PATH] [HASH]")
print("EX - ./Hash-Cracker.py /usr/share/wordlist.txt 717d3e7b9278e122e65d6240c7ea9b81")
print("")

wordlist_location = sys.argv[1]
hash_input = sys.argv[2]

print("[*] Start Cracking...")
with open(wordlist_location, 'r', encoding='latin-1') as file:
	for line in file.readlines():
		hash_md5 = hashlib.md5(line.strip().encode())
		hashed_pass_md5 = hash_md5.hexdigest()
		hash_sha256 = hashlib.sha256(line.strip().encode())
		hashed_pass_sha256 = hash_sha256.hexdigest()
		if hashed_pass_md5 == hash_input:
			print("[+] MD5 Password is: " + line.strip())
			exit(0)
		if hashed_pass_sha256 == hash_input:
			print("[+] SHA256 Password is: " + line.strip())
			exit(0)
	else:
		print("[!] No Password Found!")
		exit(0)
