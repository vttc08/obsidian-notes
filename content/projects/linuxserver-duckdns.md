Official Image: https://hub.docker.com/r/linuxserver/duckdns
Custom Github Page: https://github.com/vttc08/docker-duckdns-dynu

In the linuxserver image
- run `docker exec -it duckdns /app/duck.sh` will manually run the script
- `docker restart duckdns` will also manually run the script again

Linuxserver uses a crontab file at `/root/etc/crontabs` for scheduling
The scripts are located at `/root/app`