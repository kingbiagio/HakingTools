echo "-> ICMP Host Discovery <-"
1..15 | %{echo “192.168.1.$_”; ping -n 1 192.168.1.$_ | Select-String ttl}
