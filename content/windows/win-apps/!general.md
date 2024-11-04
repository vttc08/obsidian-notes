### General Windows Apps
There will be notes to specific apps setup.

#### Powershell 
```
winget install gnu.nano
nano $profile
```
Add these lines into PowerShell profile
``` powershell
Set-PSReadlineKeyHandler -Key ctrl+d -Function ViExit
Set-Alias which where.exe
```
- these will make terminal window exit on ctrl-d
- use the `which` command as if on Linux
Ensure the scripts folder are located at `$HOME\scripts`
- the scripts in these folder are quick scripts also used in task scheduler
- the folder contains the `.ps1` files as well as `.xml` file which is used for importing tasks in the scheduler
The scripts in that folder can also be added in powershell alias
```powershell
new-alias the-alias $env:USERPROFILE/scripts/thescript.ps1
```
#### Google Chrome
#### Extensions
**[Wayback Machine](https://chromewebstore.google.com/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak)**
Setting: General -> "Auto Save Page" if not archived "previously"

#### Firefox
**Backup profile [link](https://support.mozilla.org/en-US/kb/back-and-restore-information-firefox-profiles#w_locate-your-profile-folder)**
The profile location, go to `about:support`. It is under `Application Basics` and `Profile Folder`
`%APPDATA%\Mozilla\Firefox\Profiles`
Make sure to close Firefox before backup.
**Restore**
Copy the profile from the old machine to the new machine in the same location.
Go to the root folder and edit the file `profiles.ini`
```c
[Install308046B0AF4A39CB]
Default=Profiles/wdqvdbya.default-release
Locked=1

[Profile0]
Name=default-release
IsRelative=1
Path=Profiles/wdqvdbya.default-release

[General]
StartWithLastProfile=1
Version=2
```
- There should only be 1 profile `profile0`, delete all other profiles
- Under the `InstallXXX[Default]` and `Profile[Path]` it should reference to the profile name of the folder
To create a new profile shortcut, find the location of Firefox shortcut, then edit its target to `-p ProfileName`


**Policies**
https://gist.github.com/vttc08/4b2dbf55157a61bb2f92de01c566bc19
```powershell
mkdir -Force "C:\Program Files\Mozilla Firefox\distribution\"
wget "https://gist.githubusercontent.com/vttc08/4b2dbf55157a61bb2f92de01c566bc19/raw/0deea321e663c1215c45d4ec6e86446902e95c3c/policies.json" -O "C:\Program Files\Mozilla Firefox\distribution\policies.json"
```
**Profiles**
https://gist.github.com/jooize/5636b9eb975bde30c38b753e9f301de4
Go to `about:profiles` to create a new profile. Sign in to Firefox account and everything should sync, there is also option to import from Chrome. Once everything is setup, the profile will be stored in `%APPDATA%\Mozilla\Firefox\Profiles`. Alternative it's possible to create it via `profile.ini`.
Once the new profile is created and setup. Go to `about:config` and change these settings
- `taskbar.grouping.useprofile` create and set to true
- `browser.startup.blankwindow` set to false
To create a desktop shortcut use the flag `--no-remote -P "Profile Name"`
- the icon can be changed, the `.ico` file is located in each of the profile folder
- there is a `Firefox Master.psd` located at the root profile folder

#### Microsoft Edge
**Fix your browser managed by organization**
```powershell
taskkill /im msedge.exe /f
reg delete "HKCU\Software\Policies\Microsoft\Edge" /f
reg delete "HKLM\Software\Policies\Microsoft\Edge" /f
```

#### VSCode
Most of the configuration will be synced if logging in via Microsoft account with exception of SSH settings.
SSH settings on stored in Windows at `C:\Users\hubcc\.ssh\config`, these settings are global
Once syncthing is setup, run the powershell script located in `Documents\ssh\ssh_config\configure.ps1` to restore SSH configs
