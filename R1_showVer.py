#!/usr/bin/python3

"""
Use Netmiko to execute 'show ver' on IOS-XE CSR1000v R01.
"""
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

R01 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.103',
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
    router = ConnectHandler(**R01)
    arp_R01 = router.send_command("show ver")
    print ('-' * 8)
    print ('SHOW ARP:')
    print ('-' * 8)
    print ('\n')
    print ('R01:')
    print (arp_R01)
    print ('=' * 8)

if __name__ == "__main__":
    main()
