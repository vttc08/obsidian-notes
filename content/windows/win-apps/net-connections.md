For connecting to networked resources, eg. SMB, SSH, Wireguard
## SSH
Remember to not use strict host checking for automating ssh login.
```powershell
ssh -o StrictHostKeyChecking=no $target
```
- every subsequent logins will be immediate
## SMB
