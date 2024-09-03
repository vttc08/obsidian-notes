In the Windows installer, choose Language "English (world)", this disable all the bloatware and MS Store
- to re-enable, search for region in the settings, change back from world to US/Canada
Powershell
`Set-ExecutionPolicy Unrestricted` -> A to apply to all
Install Git using Winget
UAC -> Never Notify

Uninstall McAfee and other bloatware
Uninstall OneDrive 

`HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders`
Use RegEdit to edit the location of Documents, Download, Desktop, Pictures, Music, Videos folder to %USERPROFILE%\folder

https://support.microsoft.com/en-gb/topic/operation-to-change-a-personal-folder-location-fails-in-windows-ffb95139-6dbb-821d-27ec-62c9aaccd720
https://www.tenforums.com/tutorials/16278-enable-disable-onedrive-integration.html
[Download](https://www.tenforums.com/attachments/tutorials/31326d1439576957-onedrive-integration-enable-disable-windows-10-a-disable_onedrive_integration.reg)
Disable OneDrive using regedit to have custom location for user profile folders
```powershell
Windows Registry Editor Version 5.00  
 
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\OneDrive]  
"DisableFileSyncNGSC"=dword:00000001
```

Enable Full Context Menu
https://www.elevenforum.com/attachments/disable_show_more_options_context_menu-reg.8879/?hash=4dc0214cd4038aad11031d926f1884b5
```powershell
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32]
@=""
```

*Laptop Only*
Change the three finger tap to middle mouse button
```powershell
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\PrecisionTouchPad]
"ThreeFingerTapEnabled"=dword:00000004
```

#### Installing Apps
[!general](win-apps/!general.md)
Install Syncthing tray and Obsidian
```powershell
winget install Martchus.syncthingtray
winget install Obsidian.Obsidian
```
- restore ssh keys, music, obsidian notes with Syncthing
- default port 8384

Folders to add to Syncthing
`~\Documents\ssh`
`~\Documents\Projects`

Install Winrar
`winget install WinRar`
Configure Winrar (in the future upload to own git repo)
```powershell
wget https://gist.githubusercontent.com/MuhammadSaim/de84d1ca59952cf1efaa8c061aab81a1/raw/ca31cbda01412e85949810d52d03573af281f826/rarreg.key -O "C:\Program Files\Winrar\rarreg.key"
```
Set winrar as default for all archive (From ChatGPT)
- download SetUserFTA [[SetUserFTA & Browser]]
`SetUserFTA.exe .zip WinRar`


Install gsudo
`winget install gerardog.gsudo`

Personalization -> Colors
Choose your mode: Dark
default Windows mode: Dark
default app mode: Dark

Pin user folder C:\\Users\\hubcc into quick access

Show hidden files, show file extension

Software to be configured
Install QuickLook
Configure QuickLook to start at login (cannot be automated)

PuTTY
- backup and restore PuTTY config from the `~\Documents\ssh` folder

##### Web Browsers
[Firefox](win-apps/!general.md#Firefox)
[Chrome](win-apps/!general.md#Google%20Chrome)
Chrome
- change default browser to chrome
- [[SetUserFTA & Browser]]
- Copy the chrome data `%LOCALAPPDATA%\Google\Chrome\User Data\`
Restore Taskbar Items
Backup chrome taskbar items
`%APPDATA%\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar`
Export registry
`Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Taskband`

Discord login - cannot be automated

**Debloat**
OOShutUp
MSEdge
- disable tracking in the web
- disable personalizing advertising
Cortana
- disable and reset Cortant
Misc
- disable automatic installation of recommended Windows Store Apps
- disable meet now button
- disable sync of windows design settings
OOS has ability to export config file, settings apply need restart

Disable location tracking
```json
"Path": "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\location",
        "Name": "Value",
        "Type": "String",
        "Value": "Deny",
```
Disable telemetry CTT WinUtil
https://github.com/ChrisTitusTech/winutil/blob/8e138c38d396955570a564537b55f9ea17645ff9/config/tweaks.json#L1513
these are the tweaks in task scheduler to be disabled

BloatyNosy
Removing MS Store apps
`Get-AppxPackage -allusers SpotifyAB.SpotifyMusic | Remove-AppxPackage`
this command remove Spotify 

List of apps classified as bloatware in Windows 10 and 11
`* means wildcard*`
AD2F1837* are HP bloatware
B9ECED6F* are Asus bloatware
Microsoft.549981C3F5F10 is Cortana
Wildcard uninstallation by powershell is supported


The list of bloatware is found at `./windows/bloatware.txt`
```powershell
$apps = Get-Content -Path .\bloatware.txt

foreach ($app in $apps) {
    Get-AppxPackage -AllUsers $app | Remove-AppxPackage
}
```

Unpin all the apps from start menu (Windows 11)
Option 1:  remove/backup all the files from this location 
`%LocalAppData%\Packages\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy\LocalState`
Option 2: use a fresh start2.bin located in `./windows` folder

Disable Windows Feature Update
https://github.com/ChrisTitusTech/winutil/blob/8e138c38d396955570a564537b55f9ea17645ff9/functions/public/Invoke-WPFUpdatessecurity.ps1#L4

Remove startup apps
These are the locations that taskmgr query for apps
```
 HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

```
 HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run
```

```
 C:\Users\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
 HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```
These are the entries for which startup can be set as disabled or enabled
```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\RunHKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run
```
If an item in that location is enabled, it should have binary value of `02 00 00 00 00 00 00 00 00 00 00 00`
Change it to any value other than that to disable it.

Find a way to disable all notification for `Suggested`