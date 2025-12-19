find a process ID to kill
```sh
pidof $process
```
- By default it sends signal 15 with is SIGTERM
Kill all process by PID
```sh
killall $name
```
Kill multiple processes
```sh
kill -9 1 2 3
```