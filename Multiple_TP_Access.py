from netmiko import*
from datetime import*
import sys

vc_endpoint1 = {
    'device_type':'cisco_tp',
    'ip':'172.16.50.83',
    'username':'DISU',
    'password':'Poleoce!!',
    'port':'22',
    }
vc_endpoint2 = {
    'device_type':'cisco_tp',
    'ip':'172.16.50.82',
    'username':'DISU',
    'password':'Poleoce!!',
    'port':'22',
    }
vc_endpoint3 = {
    'device_type':'cisco_tp',
    'ip':'172.16.50.81',
    'username':'DISU',
    'password':'Poleoce!!',
    'port':'22',
    }
vc_endpoint4 = {
    'device_type':'cisco_tp',
    'ip':'172.16.50.74',
    'username':'DISU',
    'password':'Poleoce!!',
    'port':'22',
    }

vc_devices=[vc_endpoint1, vc_endpoint2, vc_endpoint3, vc_endpoint4]

start_time= datetime.now()

for video_units in vc_devices:
    ssh_connect=ConnectHandler(**video_units)
    print(ssh_connect.find_prompt())
    config_sent = ssh_connect.send_command('xstatus systemunit')
    print(config_sent)


end_time= datetime.now()

total_time = end_time - start_time
print(total_time)


