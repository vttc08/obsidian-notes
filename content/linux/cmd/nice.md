check the priority and niceness of a process
```sh
ps -l
```
higher the niceness, the more it's willing to give to other processes, ranges between -20 to 20
Change priority of process that's already running
```bash
sudo renice -10 -p $pid
```
Set priority when launching a process
```sh
nice -n $niceness $process
```