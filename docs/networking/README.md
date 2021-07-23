# Files for setting up LAN with remote controller acting as DHCP server.

- netplan/
  - while connected to your institutional network (i.e. the internet), open a terminal in your home directory (or desktop or another writable folder) and enter:
```
cat /run/systemd/resolve/resolv.conf >> defaultDNS.conf
``` 
  - then view your available interfaces with:
```
ip a s
```
