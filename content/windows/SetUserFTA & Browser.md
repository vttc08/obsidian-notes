`SetUserFTA.exe get | find .extension`
`SetUserFTA.exe .zip WinRar` will set WinRar as the default program for .zip files
Using config file (provided in the subfolder)
```yml
.zip, WinRar
.mp4, VLC
```

Find the program that you want to associate
```powershell
cmd /c assoc | findstr vlc
```
`.vlc=VLC.vlc`
For VLC, set it as such `.mp4, VLC.mp4`

**Set Default Browser**
`SetDefaultBrowser.exe` get list of available browser
`SetDefaultBrowser.exe chrome` sets it to Chrome
`SetDefaultBrowser.exe HKLM Firefox-308046B0AF4A39CB` Firefox
`SetDefaultBrowser.exe HKCU Brave.TK7WPWN46KGTJCOQ43VH7JWCPM` Brave browser with adblocking
