#!/usr/bin/python3

import sys, os, requests

print("")
print("--> HTTP SUBDOMAIN ENUMERATION <--")
print("")
print("USE - ./subdomain_enum.py [WORDLIST-PATH] [http or https] [IP/HOSTNAME]")
print("EX -  ./subdomain_enum.py /usr/share/example.txt http google.com")
print("EX -  ./subdomain_enum.py /usr/share/example.txt https google.com")
print("")

file = f"{sys.argv[1]}"
path = os.getcwd() + file
sub_list = open(file).read()
subdoms = sub_list.splitlines()

print("[+] STARTING ENUMERATION ON:",[sys.argv[3]])
for sub in subdoms:
    sub_domains = f"{sys.argv[2]}://{sub}.{sys.argv[3]}"

    try:
        requests.get(sub_domains)
    except requests.ConnectionError:
        pass
    else:
        print("[+]VALID DOMAIN: ",sub_domains)
