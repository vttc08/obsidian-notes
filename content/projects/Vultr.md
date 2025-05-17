Benchmarks
Geekbench
iperf3
Speedtest-cli
Deployment time

| Plan ID      | Type             | RAM    | Disk       | Bandwidth | Price  | Hourly Price | Location          |
| ------------ | ---------------- | ------ | ---------- | --------- | ------ | ------------ | ----------------- |
| vc2-1c-0.5gb | Standard         | 0.5 GB | 10 GB SSD  | 0.5 TB    | $3.50  | $0.005       | New York only     |
| vc2-1c-1gb   | Standard         | 1 GB   | 25 GB SSD  | 1 TB      | $5.00  | $0.007       | Seattle available |
| vhf-1c-1gb   | High Frequency   | 1 GB   | 32 GB NVMe | 1 TB      | $6.00  | $0.008       | Seattle available |
| vhp-1c-1gb   | High Performance | 1 GB   | 25 GB NVMe | 2 TB      | $6.00  | $0.008       | Seattle available |
| vc2-1c-2gb   | Standard         | 2 GB   | 55 GB SSD  | 2 TB      | $10.00 | $0.014       | Seattle available |
| vc2-2c-2gb   | Standard x2      | 2GB    |            | 3TB       | $15.00 | $0.021       | Seattle           |

## Misc
Time to deploy from API (Ubuntu and Debian)
- time between API request to successful SSH with `whoami` printed\
On GUI only Debian is available for vc2-1c-0.5

ewr + deb 12 + lowest tier = 139.23s
~~ + deb 11 = 157.02s
sea + ub22 + 1/1 = 128.38s
sea + ub24 + 1/1 = 101.10s
sea + deb11 + 1/1 = 115.19s
sea + deb12 + 1/1 = 132.33s
vc2-1c-0.5gb-ewr-2136 = 110.21s
1hf/1 + ubuntu = 70s
1hf/1 + debian = 78.30s
1hp/1 + ubuntu = 195.32s
1hp/1 + debian = 127.23s
vhf-1c-1gb-sea-2284 = 79.28s
vhf-1c-1gb-sea-2136 = 79.30s
vc2-1c-1gb-sea-2284 = 123.22s
vc2-1c-1gb-sea-2284 = 136.28s
vc2-1c-1gb-sea-2136 = 93.17s
vc2-1c-1gb-sea-2136 = 125.45s
vc2-1c-1gb-sea-2136 = 82.05s
## Network
Normal iperf
Normal speedtest
Wireguard bare metal server
- speedtest from home
- iperf wg, htop
- client: Windows 10 PC, WG app
Tailscale bare metal
- iperf3
- wget Jellyfin speedtest, htop, network monitoring
Outline VPN server, 3x-ui VLESS + WS + TLS (Caddy lego and cloudflare) and VMESS + WS
- speedtest, CPU monitoring
Caddy - is AES enabled on CPU?
Take note of disk usage
## Performance
Geekbench
Unrar, 7z benchmark
## Docker
`apt update && apt upgrade` time taken, take note of storage usage
Time to install docker, note storage
Pull the images first, before  `docker compose up -d`
Use existing data to make sure the app is running state rather than initializing
- UptimeKuma
- Authelia
- Backrest
- FileBrowser
- Wordpress + MySQL
- Tailscale
- Portainer
Lower priority
- Syncthing
- Fireshare
- JDownloader
- SFTPGo
- OpenWebUI

Measure time to deploy, afterward, measure CPU usage.