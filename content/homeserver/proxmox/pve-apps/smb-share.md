**SMB Client Linux**
`apt install cifs-utils`
`sudo mkdir /dir/to/smb/mount

Create SMB password
`nano ~/.smbcredentials` it can be anything
```shell
username=username_on_remote_server
password=pass
```

Mount the SMB share in `/etc/fstab`
```shell
//10.10.120.x/directory /dir/to/smb/mount cifs credentials=~/.smbcredentials 0 0 
```
make sure to use the credentials file

