Start a server
```sh
iperf3 -s
```
Basic test as client
```sh
iperf3 -c example.com
```
Use multiple threads
```sh
iperf3 -c example.com -P 4
```
Test download speed 
```bash
iperf3 -c example.com -R
```
Test UDP (unlimited)
- by default `iperf3` limit speed to 1M, use `-b` to change
```sh
iperf3 -c example.com -u -b 1000m
```
