Autojump or j.

Install
Autojump is included in the repo
```shell
sudo apt install autojump
```

Configure
Add these lines in `~/.bashrc` then source it
```bash
if [ -f /usr/share/autojump/autojump.bash ];
then
  . /usr/share/autojump/autojump.bash
fi
```
The default keyboard shortcut is `j`

Edit weights
- sometimes autojump will jump to directory that is not wanted
The weights are stored in a file `~/.loca/share/autojump/autojump.txt`
```txt
84.85281374238572       /home/karis/Templates
150.332963783729        /home/karis/docker
```
- simply remove the line or change the weight value manually