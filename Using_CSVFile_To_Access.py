from netmiko import*
from datetime import*
import csv

vc_input_file="Test_file.csv" #assign variable for file

#Creating empty list
vc_lst=[]

#accessing file using "with" statement
with open(vc_input_file,'r') as vcfile:
    for vcunits in csv.DictReader(vcfile): #Reading input data using and converting to dictionary
        print(vcunits)
        vc_lst.append(vcunits)             #Adding dictionary to empty list
print(vc_lst)                              #list output
start_time= datetime.now()       
for video_units in vc_lst:                 #loop to initiate connections for all items in list
    ssh_connect=ConnectHandler(**video_units)
    print(ssh_connect.find_prompt())       #Connection output
    config_sent = ssh_connect.send_command('xstatus systemunit')    #Sending command to accessed endpoints
    print(config_sent)
end_time= datetime.now()

total_time = end_time - start_time
print(total_time)           #Time taken for all




