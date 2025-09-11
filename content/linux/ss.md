TCP connections that are currently listening
```bash
ss -lt
```
- use `u` for UDP and `a` for all connections even RAW, UNIX sockets
Watch statistics of  total system connection
```bash
watch ss -s
```
Specify IPv4 or v6
```bash
ss -46
```
Whether SSH port is listening
```bash
ss -at '( dport = :22 or sport = :22 )'
```