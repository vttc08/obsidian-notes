This is the command to download [cheat](https://github.com/cheat/cheat/releases)
```bash
cd /tmp \
  && wget https://github.com/cheat/cheat/releases/download/4.4.2/cheat-linux-amd64.gz \
  && gunzip cheat-linux-amd64.gz \
  && chmod +x cheat-linux-amd64 \
  && sudo mv cheat-linux-amd64 /usr/local/bin/cheat
```

The cheats are stored as `community` and `personal`, which both are located in `~/.config/cheat/cheatsheets`