Force resolve specific domain
```bash
curl https://domain.ddns --resolve domain.ddns:443:127.0.0.1
```
Use SOCKS5 proxy
```bash
curl -v --socks5 10.10.120.191:10808 ipconfig.me
```
Resolve hostname using SOCKS5
```bash
curl -v --socks5-hostname 10.10.120.191:10808 ipconfig.me
```
