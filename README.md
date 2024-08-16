# cloud-ip-receiver

A simple pyhon app to listen curl requests.

```powershell
$ip = (Invoke-WebRequest -Uri "https://ip.bayhan.ca/ip" -Method Get -UseBasicParsing).Content ; $payload = @{ ip = $ip } | ConvertTo-Json ; Invoke-WebRequest -Uri "http://localhost:5001/update-ip" -Method Post -Header @{"Content-Type" = "application/json"} -Body $payload
```

```bash
curl -X POST -H "Content-Type: application/json" -d '{"ip": "$(curl https://ip.bayhan.ca/ip)"}' http://localhost:5001/update-ip
```
