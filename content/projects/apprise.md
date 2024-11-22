https://github.com/caronc/apprise/wiki/CLI_Usage
```python
pip install apprise --upgrade
```

Apprise will read from stdin as body
```bash
uptime | apprise url
```
Apprise on attach files on supported services
```bash
apprise -a file.zip
```
- the file path is relative to where the command is executed
Interpret line break will interpret `\n` in line break and in the sent message will be in 2 lines

Notification types:
```bash
apprise -n info/warning/error/success
```

## Config File
It is possible to store the configuration file in home directory as `~/.apprise`
After the file is created now apprise can be used with tags as defined in the configuration file, the file can include from other servers
```bash
apprise -b "test" --tag=all
```
```nginx
include http://10.10.120.12:7000/get/apprise
```

## Markdown
On services supporting markdown, eg. Discord. Markdown can be sent in terminal.
```bash
cat << _EOF | apprise --input-format=markdown "url"
\`code block\`
# Markdown text
```
```bash
cat file.md | apprise --input-format=markdown "url"
```
- the code block backtick needs to be escaped with `\` in bash 
- alternative a file can be used
Alternatively HTML can be used, but not all services support it
### Discord
https://github.com/caronc/apprise/wiki/Notify_discord
```shell
apprise -b "Text message" "discord://userid/webhook?avatar_url="
```
- user ID and webhook URL are provided by the discord channel
- use `avatar_url` and it will only change for Discord
For discord, it is preferred to warp the apprise URL in quotes.
#### Markdown
The discord format to markdown as `?format=markdown` is different as apprise `--input-format=markdown`
When using this option, it will wrap the markdown in an embed rather than just code. The embed will have a color based on what type of notifications (error, warning, success, info).
![](assets/Pasted%20image%2020241112162517.png)
It's not possible in CLI to change the Apprise URL in Discord notification.

## API-Server
[apprise-api](../!documentation/Docker%20Apps/notification/apprise-api.md)

## Mailrise
[apprise-api](../!documentation/Docker%20Apps/notification/apprise-api.md#Mailrise)
