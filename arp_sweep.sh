#!/bin/sh

if [ "$#" -ne 1 ]; then
echo "-> ARP Host Discovery <-"
echo "Usage: sudo ./arp_sweep.sh [Network-ID]"
echo "Example: sudo ./arp_sweep.sh 192.168.1.0"
exit
fi

prefix=$(echo $1 | cut -d '.' -f 1-3)

for addr in $(seq 1 254); do
arping -w 3 -c 1 $prefix.$addr | grep "bytes from" &
done

sleep 5
