#!/bin/bash

if [ "$#" -ne 1 ]; then
echo "-> TCP Port Scan <-"
echo "Usage: ./tcp_scan.sh [IP]"
echo "Example: ./tcp_scan.sh 192.168.1.10"
exit
fi

host=$1
for i in $(seq 1 65535);
do (bash -c "echo >& /dev/tcp/$host/$i") >/dev/null 2>&1 && echo $i TCP is open; 
done
