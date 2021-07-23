# Files for setting up LAN with remote controller acting as DHCP server.

- netplan/
  - while connected to your institutional network (i.e. the internet), open a terminal in your home directory (or desktop or another writable folder) and enter these commands to store files with your default network information.
```
cat /run/systemd/resolve/resolv.conf > defaultDNS.conf
echo $(ip -a route) > ipRoute.conf
```
  - then view your available interfaces with:
```
ip a s
```
