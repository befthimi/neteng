#!/usr/bin/python3.6

from jinja2 import Environment, FileSystemLoader
#This line uses the current directory
file_loader = FileSystemLoader('jinja_templates')
#Load the environment
env = Environment(loader=file_loader)
template = env.get_template('bgp_template.j2')
#Add the variables
output = template.render(local_asn='1111', bgp_neighbor='192.168.1.1', remote_asn='2222')
#Print the output
print(output)
