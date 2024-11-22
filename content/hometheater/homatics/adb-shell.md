All the commands listed here assumes it's in a adb shell, to execute the command without a shell, add `adb shell` to the front of each commands
Go to adb shell via `adb shell` and use this to list all the package names
```c
pm list packages | grep -Ei "app1|app2"
```
```c
pm uninstall -k --user 0 <package-name>
```

List of problematic apps
```c
com.google.android.youtube.tv
com.google.android.youtube.tvmusic
com.netflix.ninja
com.amazon.amazonvideo.livingroom
```

Disable Default Launcher
```c
pm disable-user --user 0 com.google.android.tvlauncher
```

Disable Google Play Protect (untested), this is needed to install SmartTube and other Chinese apps
```c
settings put global package_verifier_user_consent -1
```

Launch an app
- first query the app and find out its package name
```c
monkey -p com.app.package 1
```
- this command will open the app on Android device by package name

Input Text
```c
input text "abc\ dcf\ "
```
- spaces needs to be escaped via `\`
Input Tap
```c
input tap x y
```
It also work with `keyevent`

Record screen
```c
screenrecord "/sdcard/rec.mp4"
```