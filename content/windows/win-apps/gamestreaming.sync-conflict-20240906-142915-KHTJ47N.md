This will be moved to documentation later to windows.

Sunshine
```powershell
winget install lizardbyte.sunshine
```
Installation directory: `C:\Program Files\Sunshine`
Because GameStream only available in old GeForce experience
https://github.com/LizardByte/Sunshine/releases
Set admin password, default port 47790
Network -> enable UPnP (if router support it)
https://docs.lizardbyte.dev/projects/sunshine/en/latest/index.html ^93cc45

Custom Resolution
To implement custom resolution, need to download [QRes](https://www.majorgeeks.com/files/details/qres.html). and place the executable into sunshine [installation directory](#^93cc45).
Implement the custom resolution in Nvidia control panel. All the client resolutions must be implemented beforehand
- `Display` -> `Change Resolution` -> `Customize`
- Turn on `Enable resolutions no exposed by the display` and create custom resolution
- Add the resolution and frame rate accordingly
![](assets/Pasted%20image%2020240906140901.png)
For each applications to be added for custom resolution: Go to `Edit` -> `Command Preparation`
Do command
```shell
cmd /C "C:\Program Files\Sunshine\QRes.exe" /x:%SUNSHINE_CLIENT_WIDTH% /y:%SUNSHINE_CLIENT_HEIGHT% /r:%SUNSHINE_CLIENT_FPS%
```
Undo command
```shell
cmd /C "C:\Program Files\Sunshine\QRes.exe" /x:2560 /y:1440 /r:165
```

Moonlight
Android download on FDroid
Input > Use touchscreen as a trackpad (this toggle switch between [modes](https://github.com/moonlight-stream/moonlight-docs/wiki/Setup-Guide#keyboardmousegamepad-input-options))
Not possible to do on-screen keyboard control
Windows
```powershell
winget install MoonlightGameStreamingProject.Moonlight
```

Steam Link
Can play on touchscreen, but only limited games can work.