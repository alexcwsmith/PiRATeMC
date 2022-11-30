#!/bin/bash
mkdir ~/Desktop/networkBackups/
echo "Created folder at $HOME/Desktop/networkBacksup/ and writing files there"
$(echo "hostname -I") > ~/Desktop/networkBackups/IPaddr.conf
ip route | grep default | tee ~/Desktop/networkBackups/ip_route.conf
ip a s | grep -e “<” grep -e “inet” | tee ~/Desktop/networkBackups/ip_a_s.conf
cat /etc/resolv.conf | grep nameserver | tee ~/Desktop/networkBackups/resolvconf.conf
cp /etc/netplan/*.yaml ~/Desktop/networkBackups/
cp /etc/dhcp/dhcpd.conf ~/Desktop/networkBackups/
cp /etc/default/isc-dhcp-server ~/Desktop/networkBackups/
cp /etc/default/bind9 ~/Desktop/networkBackups/
exit
