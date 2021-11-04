#!/usr/bin/python3
# sudo apt install python3-pyfiglet

import hashlib
import pyfiglet
import sys

ascii_banner = pyfiglet.figlet_format("HASH CRACKER", font="digital")
print(ascii_banner)
print("Hash Supported: NTLM, MD5, SHA-256\n")
print("USE - ./Hash-Cracker.py [WORDLIST-PATH] [HASH]")
print("EX - ./Hash-Cracker.py /usr/share/wordlists/rockyou.txt a332233d395c415a99c6b16a2348c129")
print("")

wordlist_location = sys.argv[1]
hash_input = sys.argv[2]

print("[*] Start Cracking...")
with open(wordlist_location, 'r', encoding='latin-1') as file:  #encoding="ISO-8859-1"
	for line in file.readlines():
		
		hash_NTLM = hashlib.new('md4', line.strip().encode('utf-16le')).digest()
		
		hash_md5 = hashlib.md5(line.strip().encode())
		hashed_pass_md5 = hash_md5.hexdigest()
		
		hash_sha256 = hashlib.sha256(line.strip().encode())
		hashed_pass_sha256 = hash_sha256.hexdigest()
		
		if binascii.hexlify(hash_NTLM).decode('utf-8') == hash_input:
			print(("[+] NTLM Password is: " + line.strip()))
			exit(0)
		
		if hashed_pass_md5 == hash_input:
			print("[+] MD5 Password is: " + line.strip())
			exit(0)
			
		if hashed_pass_sha256 == hash_input:
			print("[+] SHA256 Password is: " + line.strip())
			exit(0)
	else:
		print("[!] No Password Found!")
		exit(0)
