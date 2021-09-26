from netmiko import*
import getpass

vc_endpoint = {
    'device_type':'cisco_tp',
    'ip':'',
    'username':'',
    'password':'',
    'port':'22',
    }

hostname = input('Target IP:')
target_user = input('Enter username:')
target_pass= input('Enter password:')

vc_endpoint['ip']= str(hostname)
vc_endpoint['username']=target_user
vc_endpoint['password']= str(target_pass)

ssh_connect=ConnectHandler(**vc_endpoint)

print(ssh_connect.find_prompt())


command_to_ep=input('send command:')

config_sent = ssh_connect.send_command(command_to_ep)

print(config_sent)
