#!/usr/bin/python3
# sudo apt install python3-pyfiglet

import sys
import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Python TCP Port Scanner\n", font="digital")
print(ascii_banner)

print("USE - ./port_scannerTCP.py [HOSTNAME/IP]")
print("EX - ./port_scannerTCP.py pentestvm.local")

ip = sys.argv[1] 
open_ports =[] 
ports = range(1, 65535)

def probe_port(ip, port, result = 1):  
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports:
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 

if open_ports: 
  print ("TCP Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("No TCP Ports are open: ")
