Print information to the screen as well as to a file
```bash
echo "something" | tee file.txt file2 # print to both stdin and file
```
- overwrite the file by default, `-a` to append
Solve permission issues with tee with sudo, need to put it in the tee
```bash
echo "" | sudo tee
```