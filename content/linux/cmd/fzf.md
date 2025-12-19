Install
```bash
sudo apt install fzf -y
```

When executing fzf, it will open a select box. Once selected, the filename will be the output.

Select multiple
```bash
fzf -m # multi select
```
- use tab, shift-tab to select or deselect
- the selection will be output as a list separated by space

Case Insensitive
```bash
fzf -i # use +i for case sensitive
```

