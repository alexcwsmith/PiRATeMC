# Files for setting up LAN with remote controller acting as DHCP server.
### Before getting started with network reconfiguration, install the necessary packages to run a DHCP server and PiRATeMC:
```
sudo apt install openssh-server
sudo apt install isc-dhcp-server
sudo apt install bind9
sudo apt install clusterssh
```

- netplan/
  - while connected to your institutional network (i.e. the internet), open a terminal in your home directory (or desktop or another writable folder) and enter these commands to store files with your default network information.
```
echo $(hostname -I) > defaultIPaddress.conf
cat /run/systemd/resolve/resolv.conf > defaultDNS.conf
echo $(ip -a route) > ipRoute.conf
```
  - then view your available interfaces with:
```
ip a s
```
In this example you can see I have 5 network adapters (in additon to lo which is localhost): enp3s0, enp4s0, enp5s0, enp6s0, and eno1. The four that begin with 'enp' are from a 4-port networking card I added to this computer, and 'eno1' is the ethernet port attached to the motherboard.
![ip_a_s](https://user-images.githubusercontent.com/47009665/126724644-a0de3f86-f35d-495a-9067-60a2d824e163.png)

Modify the file netplan/01-network-manager-all.yaml, the first ethernet configurtion (enp6s0) is for my institutional network connection. You should replace the IP address on line 6 with your own (it should still end with /24), and replace the default gateway with the gateway shown in ipRoute.conf, and the nameservers in defaultDNS.conf

In the second section (enp5s0) all you need to modify is the name of the network adapter. The rest can be left the same, and the remote controller computer will be assigned a second IP address, 10.1.1.243, which will also function as a DNS, giving it the ability to assign IP addresses to the RPis.

After you have made these changes, run:
```
sudo netplan apply
```
