Pinggy
```bash
ssh -p 443 -R0:localhost:56789 -o StrictHostKeyChecking=no -o ServerAliveInterval=30 6Eyd7skanEB@free.pinggy.io
```
Tailscale funnel
https://tailscale.com/kb/1223/funnel
must be localhost
```bash
sudo tailscale funnel localhost:port
```
Devtunnel
localhost only
```bash
devtunnel host -a -p 56789 
```
Serveo
```bash
ssh -R 80:localhost:3000 serveo.net
```

Client behavior
V2RayNG, Nekobox do not have subscription tracking
Only hiddify does
It is done via appending 
```
#reality-18mwh38z-204.80MB%F0%9F%93%8A-23H%E2%8F%B3
```