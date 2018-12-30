#!/usr/bin python3

"""
Use Netmiko to execute 'show arp' on asa-fw01.
"""
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

asafw01 = {
    'device_type': 'cisco_asa',
    'ip': '192.168.1.59',
    'username': 'befthimi',
    'password': password,
}

#pynet2 = {
#    'device_type': 'cisco_ios',
#    'ip': '50.76.53.27',
#    'username': 'pyclass',
#    'password': password,
#    'port': 8022,
#}

def main():
    """
    main function
    """
    fw01 = ConnectHandler(**asafw01)
    arp_fw01 = fw01.send_command("show arp")
    print ('-' * 8)
    print ('SHOW ARP:')
    print ('-' * 8)
    print ('\n')
    print ('ASA-FW01:')
    print (arp_fw01)
    print ('=' * 8)

if __name__ == "__main__":
    main()
