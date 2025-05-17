```python
import subprocess
```

## Linux

```python
subprocess.run("pwd") # simply running a command
# returns CompletedProcess not the output
```

    /mnt/c/Users/hubcc/Documents/VSCode/notes/python

    CompletedProcess(args='pwd', returncode=0)

```python
# use a shell command
subprocess.run("ls -l", shell=True) # running a command with shell and with arguments
# if not using shell, then everything has to be a list ["ls","-la"]
```

```python
# if not using shell, the commands can be split using shlex
import shlex
command = "ls -l"
args = shlex.split(command)
```

```python
# Process object and capture output
proc = subprocess.run("ls -l", shell=True, capture_output=True, text=True) # running a command with shell and with arguments
# text=True convert the output to string
proc.args # the arguments used to call the process
proc.returncode # the return code of the process
proc.stdout # the standard output of the process
proc.stderr # the standard error of the process
```

    ''

When capturing via `capture_output=True`, the output is not displayed in the terminal.
If there are errors in shell command, it does not cause Python to error.

```python
new = subprocess.run("ls -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
# stdout=subprocess.PIPE captures the output and stderr=subprocess.DEVNULL ignores the error output
```

```python
err = subprocess.run("sdfjlsdf", check=True)
# check=True will raise an exception if the command fails
```

```python
err = subprocess.run("notounfd", shell=True, capture_output=True)
err.stdout
```

    b''

```python
# pipe and input from another command
p2 = subprocess.run("grep 'test'", shell=True, input="test\nnotest\n", capture_output=True, text=True)
p2.stdout # the output of the command
```

    'test\nnotest\n'

### Run vs Popen
Subprocess.run() is a higher-level interface that is easier to use for most common use cases. It waits for the command to complete and returns a CompletedProcess object, which contains the output, error messages, and return code. It is a good choice for most simple use cases.

```python
p3 = subprocess.Popen("./test.sh", shell=True, text=True)
p4 = subprocess.Popen("./test.sh", shell=True, text=True)
print("this should be printed before the script ends")
# Popen creates a new process
```

```python
cf = subprocess.Popen("python cloudflare.py", shell=True)
```

    2025-04-25T04:50:53Z INF +--------------------------------------------------------------------------------------------+
    2025-04-25T04:50:53Z INF |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
    2025-04-25T04:50:53Z INF |  https://missouri-diary-analyze-courage.trycloudflare.com                                  |

```python
cf.poll() # wait for the process to finish
# return None if it's running, else return the return code
```
