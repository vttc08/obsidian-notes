Screen allow you to run terminal inside a terminal.

To start a new session
```bash
screen -S name
```
To detach, press `Ctrl-A` then `D`
To kill that session, press `Ctrl-A` then `K` and `y`
Alternate way to kill a screen session
```bash
screen -XS name quit 
```

List running screen sessions
```bash
screen -ls
```
Reconnect to a session by name
```bash
screen -r name
```
