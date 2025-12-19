Show information with color
```bash
ip -c a
```
Show specific device
```bash
ip a show dev enp2s0
```
Make an interface down
```bash
sudo ip link set enp2s0 down
```
- use up to reverse the proxy
Add IP address on interface
```bash
sudo ip addr add 192.168.0.123/24 dev enp2s0
```
- use del instead of add to delete an IP
Add an route
```bash
sudo ip route add 192.168.0.1/24 via 172.16.250.1 dev enp2s0
```
- use 172.16.250.1 to access 192.168.0.1/24 on enp2s0
Watch for dropped packet and net statistics
```bash
watch ip -s link show enp2s0
```