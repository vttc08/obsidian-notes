Install (old version from package repo), it will also install autocomplete
```bash
sudo apt install tealdeer
```
Latest binary
```
https://github.com/tealdeer-rs/tealdeer/releases/latest
```
Replace
```bash
sudo cp tealdeer-linux-x86_64-musl /usr/bin/tldr 
```
Install autocompletion
```bash
wget https://github.com/tealdeer-rs/tealdeer/releases/download/v1.7.2/completions_bash
sudo mv completions_bash /usr/share/bash-completion/completions/tldr
```
Default configuration
```bash
tldr --seed-config
```
Default repo location
```bash
~/.cache/tealdeer/tldr-pages/
```
Custom page location
```bash
~/.local/share/tealdeer/pages/
```
Make sure it exists
```bash
mkdir -p ~/.local/share/tealdeer/pages/
```
Naming convention
```bash
mycmd.page.md # replace default
mycmd.patch.md # append at bottom
```
Compact display
```bash
~/.config/tealdeer/config.toml
[display]
compact = true
```
TLDR fzf
```bash
alias tldf='tldr --list | fzf --preview "tldr {1} --color=always" --preview-window=right,75% | xargs tldr'
```