echo "-> ICMP Host Discovery <-"
echo ""
1..15 | % {echo "10.10.10.$_"; ping -n 1 10.10.10.$_ | Select-String ttl}
echo ""
echo "-> Finish <-"
