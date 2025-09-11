> journalctl check for logs that process produce

Get real-time logs
```bash
journalctl -f
```
Get specific process logs
```bash
sudo journalctl -u jellyfin -f
```
Limit time ranges using since and until
```bash
journalctl -S "2025-06-01 12:00:00" -U "1 hour ago"
```
- also possible to use 1 hour ago, yesterday
View log from a specific user
```bash
journalctl _UID=1000
```
Clear logs after certain size or time
```bash
sudo journalctl --vacuum-time 2d
sudo journalctl --vacuum-size 500M
```
Check log size
```bash
sudo journalctl --disk-usage
```
