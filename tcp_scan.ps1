echo "-> TCP Scan <-"
echo "USE: .\tcp_scan.ps1 IP"
echo ""
$target = $args[0]
#1..1024 | %{echo ((New-Object Net.Sockets.TcpClient).Connect(“$target”, $_)) “TCP Open port on - $_”} 2>$null
20,21,22,25,53,80,88,110,135,139,143,389,443,445,1433,3306,3389,5985,5986,8080 | %{echo ((New-Object Net.Sockets.TcpClient).Connect(“$target”, $_)) “TCP Open port on - $_”} 2>$null
