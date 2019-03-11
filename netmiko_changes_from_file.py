#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

R01 = {
    "host": "192.168.1.32",
    "username": "admin",
    "password": getpass(),
    "device_type": "cisco_ios",
}

cfg_file = "config_changes.txt"
net_connect = Netmiko(**R01)

# routing table before change #
command = "show ip route"
print('routes PRE changes')
print(net_connect.find_prompt())
pre_routes = net_connect.send_command(command) 
print(pre_routes)
print()

# make changes #
print()
print(net_connect.find_prompt())
output = net_connect.send_config_from_file(cfg_file)
print(output)
print()

# routing table after changes #
print('routes POST changes')
print(net_connect.find_prompt())
post_routes = net_connect.send_command(command)
print(post_routes)
print()


net_connect.save_config()
net_connect.disconnect()


