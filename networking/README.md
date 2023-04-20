# Files for setting up LAN with remote controller acting as DHCP server.
## Before getting started with network reconfiguration, install the necessary packages to run a DHCP server and PiRATeMC:
```
sudo apt install openssh-server
sudo apt install isc-dhcp-server
sudo apt install bind9
sudo apt install clusterssh
```
### Step 1: modify the network manager / netplan
- while connected to your institutional network (i.e. the internet), open a terminal in your home directory (or desktop or another writable folder) and run the writeNetworkConfigs.sh file found in this folder. This will make a folder on your desktop called 'networkBackups' and will run several commands to store files with your default network information, and to back up these files in case you need to revert to the original state. A summary of what can be found here is:

```
IPaddr.conf - contains all active IP addresses.
ip_a\_s.conf - shows information about all interfaces. 
ip_route.conf - shows gateway information for all active interfaces.
```
  - then view your available interfaces with:
```
ip a s
```
In this example you can see I have 5 network adapters (in additon to lo which is localhost): enp3s0, enp4s0, enp5s0, enp6s0, and eno1. The four that begin with 'enp' are from a 4-port networking card I added to this computer, and 'eno1' is the ethernet port attached to the motherboard.

![ip_a_s](https://user-images.githubusercontent.com/47009665/126724644-a0de3f86-f35d-495a-9067-60a2d824e163.png)

Modify the file 01-network-manager-all.yaml found in this repo, the first ethernet configuration (enp6s0) is for my institutional network connection. You should replace the IP address on line 6 with your own. It most likely will still end in /24, but find the IP address in ip_a\_s.conf and verify this, as it may end in /23 or /22. Replace the address after gateway4: with the gateway shown in ip\_route.conf. Your nameserver address can be found in resolvconf.conf.

In the second section (here enp5s0) all you need to modify is the name of the network adapter, which you can find in the ip_a\_s.conf file. The rest can be left the same, and the remote controller computer will be assigned a second IP address, 10.1.1.243, which will also function as a DNS, giving it the ability to assign IP addresses to the RPis.

After you have made these changes, run the following two commands to copy this file /etc/netplan/ and apply the changes.
```
sudo cp 01-network-manager-all.yaml /etc/netplan/
sudo netplan apply
```

If this is successfully there will be no output from applying the changes.

### Step 2: modify /etc/dhcp/dhcpd.conf
  - assuming you have assigned the remote controller the same static IP address as here (10.1.1.243), you can simply copy the dhcpd.conf file from this repo into your /etc/dhcp/ folder with:
```
sudo cp dhcpd.conf /etc/dhcp/dhcpd.conf
```

### Step 3: modify /etc/default/isc-dhcp-server
  - The only change to make in the isc-dhcp-server file in this repo is the name of the network adapter (here enp5s0), and then you can simply copy the file from this repo into your /etc/default/ folder:
```
sudo cp isc-dhcp-server /etc/default/isc-dhcp-server
```

### Step 4 Copy named.conf.options file to /etc/bind9:
```
sudo cp named.conf.options /etc/bind9/named.conf.options
```
### Finally, start these services:
```
sudo systemctl start isc-dhcp-server
sudo systemctl start bind9
```

- Reboot the computer, then while plugged into both the institutional network and the network switch that is connected to several powered-on RPis, run:
```
dhcp-lease-list
````

and it should appear something like this:

![dhcp-lease-list](https://user-images.githubusercontent.com/47009665/126725844-24582f89-86d2-4611-9da2-5bfe902df530.png)

### Assigning static IPs (optional)
The IP addresses assigned are relatively stable over long periods of time if the devices are left on and connected. However, if you would like to assign static IP addresses, you can do so with the dhcpd.conf file by adding the MAC addresses, hostnames, and desired IP address for each device. A template for how to do that can be found here at dhcpd_staticIPs.conf.
