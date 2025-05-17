https://youtu.be/CXj-ID33MhU
https://github.com/apernet/hysteria

Hysteria2
Installation
```bash
bash <(curl -fsSL https://get.hy2.sh/)
```
or use the binary
```bash
/etc/hysteria/config.yaml # configuratin
/etc/systemd/system/multi-user.target.wants/hyserteria-server.service # systemd unit
```

Configuration
config.yaml in the folder of hysteria

Client
V2RayN Windows
- need hy2 binary on Windows
- place the binary into `$V2RayInstall/bin/hysteria`
Sing-box2 support hy2 out of box, both Android and Windowsf

Uses UDP rather than TCP
- no congestion control
- ignore any congestion control

Bandwidth
- Client up = server down
- Client down = server up
- take the lowest
If either no bandwidth is provided by the client or `ignoreClientBandwidth: true` on server, will use BBR.