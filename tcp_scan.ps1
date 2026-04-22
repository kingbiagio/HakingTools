Write-Output "-> TCP Scan <-"
Write-Output "Usage: .\tcp_scan.ps1 <IP>"
Write-Output ""

$target = $args[0]

# lista di porte
$commonPorts = @(20,21,22,25,53,80,88,110,135,139,143,389,443,445,1433,3306,3389,5985,5986,8080)

function Test-Port {
    param (
        [string]$ip,
        [int]$port
    )
    try {
        $tcpClient = New-Object System.Net.Sockets.TcpClient
        $connectTask = $tcpClient.ConnectAsync($ip, $port)
        if ($connectTask.Wait(1000) -and $tcpClient.Connected) {
            Write-Output "TCP: $port is OPEN on $ip"
        }
        $tcpClient.Close()
    } catch {
        # Gestione errori
    }
}

foreach ($port in $commonPorts) {
    Test-Port -ip $target -port $port
}
