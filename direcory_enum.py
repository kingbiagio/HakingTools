#!/usr/bin/python3

import requests, sys, os
print("")
print("--> DIRECTORY ENUMERATION <--")
print("")
print("USE - ./directory_enum.py [WORDLIST-PATH] [http or https] [IP/HOSTNAME][EXTENSION]")
print("EX -  ./directory_enum.py /usr/share/example.txt http google.com html")
print("EX -  ./directory_enum.py /usr/share/example.txt https google.com html")
print("")

file = f"{sys.argv[1]}"
path = os.getcwd() + file
sub_list = open(file).read()
directories = sub_list.splitlines()

print("[+] STARTING ENUMERATION ON:",[sys.argv[3]])

for dir in directories:
    dir_enum = f"{sys.argv[2]}://{sys.argv[3]}/{dir}.{sys.argv[4]}"
    r = requests.get(dir_enum)
    if r.status_code==404:
        pass
    else:
        print("[+]VALID DIRECTORY: ", dir_enum)
