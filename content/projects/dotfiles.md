Tabby
```bash
export PS1="$PS1\[\e]1337;CurrentDir="'$(pwd)\a\]'
```

Vim
- change tab to width of 2, autoindent, mouse mode etc
- saved in `~/.vimrc`
- the file will be compatible with both Linux and Windows
In Windows Terminal specifically, Ctrl-V must be unbound
`keybindings`
```json
{"id": "unbound", "keys": "ctrl+v"},
```
Additional configuration needed in powershell for Windows paste to work
```bash
set pastetoggle=<F2>
```
For transparent effect, but cursor cannot be transparent
```bash
autocmd vimenter * hi Normal guibg=NONE ctermbg=NONE
```
- but it's not possible to make the cursor transparent
Windows powershell specific keybinding
```bash
nnoremap <M-Up> :m .-2<CR>==
xnoremap <M-Up> :m '<-2<CR>gv=gv
nnoremap <M-Down> :m .+1<CR>==
xnoremap <M-Down> :m '>+1<CR>gv=gv
```
Undofile
```bash
set undofile
set undodir=~/.vim/undo//
```
Copy from remote clipboard
```bash
" Copy via osc52
source ~/.vim/bundle/vim-osc52/plugin/osc52.vim
vmap <C-c> y:call SendViaOSC52(getreg('"'))<cr>
```
- need to clone from repo plugin
```bash
git clone https://github.com/fcpg/vim-osc52 ~/.vim/bundle/vim-osc52
```
On windows natively
```bash
set clipboard=unnamedplus
```
- select a line, click `"+y`

ZSH
Install using package manager
Plugin manager
- zinit
Prompt
- oh my posh

Configuration
both `.bashrc` and `.zshrc` points to `.bash_aliases` which consists of common config and variable that works for both

.zshrc
- alias `.` to source

bash_aliases
- PUID/PGID
- ll, grep and other color command
- docker related commands
- .. command

OMP
Install
```bash
sudo apt install unzip -y
curl -s https://ohmyposh.dev/install.sh | bash -s
mkdir -p ~/.config/ohmyposh
```
Place this 
```bash
eval "$(oh-my-posh init zsh --config ~/.config/ohmyposh/omp.toml)"
```
Export configuration
```bash
oh-my-posh config export --format yaml --output ~/.config/ohmyposh/omp.yaml
```
Configuration require manually specifying the file
- the folder must exist before the export

Zoxide

Netdevice
```bash
sudo iftop -i $(ip --color=never -o r get 8.8.8.8 | awk '{print $5}')
```

Tmux
By default, Tmux v3.5 will have error when used with Windows terminal, as it sends random data when it tries to start itself, earlier versions or latest 3.6a do not have such issues.
This could fix it but it will make Vim feel slower
```bash
set -g escape-time 500
set -g focus-events off
```
The better alternative is to use a [portable tmux build](https://github.com/mjakob-gh/build-static-tmux/releases/tag/v3.6a) that work across Linux distros.
- or use [3.3a](https://github.com/mjakob-gh/build-static-tmux/releases/download/v3.3a/tmux.linux-amd64.gz)
```bash
wget https://github.com/mjakob-gh/build-static-tmux/releases/download/v3.6a/tmux.linux-amd64.gz
gzip -d tmux.linux-amd64.gz
chmod +x tmux.linux-amd64
tmux=$(which tmux); sudo cp tmux.linux-amd64 ${tmux:-/usr/local/bin/tmux}
rm tmux.linux-amd64.gz
```

For compatibility of tmux and vim on server
```bash
set ttymouse=xterm2
```
```bash
set -g allow-passthrough on
```
- allow responsive mouse movement and passthrough osc52 from vim to tmux to system


What to manage
Vim and nano rc 
Tmux configuration 
Bash rc and aliases
Ssh config secret
Ssh keys secret
