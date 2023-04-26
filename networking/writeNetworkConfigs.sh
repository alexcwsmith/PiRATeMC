#!/bin/bash
[ -d "$HOME/Desktop/networkBackups/" ] && echo "networkBackups folder already found on desktop, overwriting contents"
[ ! -d "$HOME/Desktop/networkBackups/" ] && mkdir $HOME/Desktop/networkBackups/
ip a s | grep -e "<" -e "inet" | tee $HOME/Desktop/networkBackups/ip_a_s.conf
$(echo "hostname -I") > $HOME/Desktop/networkBackups/IPaddr.conf
ip route | grep default | tee $HOME/Desktop/networkBackups/ip_route.conf
cat /etc/resolv.conf | grep nameserver | tee $HOME/Desktop/networkBackups/resolvconf.conf
cp /etc/netplan/*.yaml $HOME/Desktop/networkBackups/
cp /etc/dhcp/dhcpd.conf $HOME/Desktop/networkBackups/
cp /etc/default/isc-dhcp-server $HOME/Desktop/networkBackups/
cp /etc/default/bind9 $HOME/Desktop/networkBackups/
exit
