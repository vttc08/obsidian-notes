For connecting to networked resources, eg. SMB, SSH, Wireguard
## SSH
Remember to not use strict host checking for automating ssh login.
```powershell
ssh -o StrictHostKeyChecking=no $target
```
- every subsequent logins will be immediate
### WindTerm
https://github.com/kingToolbox/WindTerm/releases
Useful modern tool for managing many SSH connections on PC.
The app is only portable, only installed and updated from Github
Caveat
- cannot immediately use it, must enable auto-login every time when connecting to a new server
By default the saves location on Windows is
```
~/.wind
```
## SMB
## Iperf3
Iperf used for network testing, for instruction on how to use instead of installation refer to [iperf3](../../linux/iperf3.md)
```powershell
winget install ar51an.iperf3
```