from netmiko import*
from datetime import*
import csv


#assign variable for file

vc_input_file="Test_file.csv" 
command_file="commands.txt"

#Creating empty lists

vc_lst=[]
commands_to_ep=[]


with open(command_file,'r') as ep_commands: #parsing text command file and appending them to list
    for lines in ep_commands:
        commands_to_ep.append(lines)



#accessing file using "with" statement
with open(vc_input_file,'r') as vcfile:
    for vcunits in csv.DictReader(vcfile): #Reading input data using and converting to dictionary
        vc_lst.append(vcunits)             #Adding dictionary to empty list



start_time= datetime.now()                 #Starting of main script


for video_units in vc_lst:                 #loop to initiate connections for all items in list
    ssh_connect=ConnectHandler(**video_units)
    print("Accessing Video Unit: {}".format(video_units['ip']))
    print(ssh_connect.find_prompt())       #Connection output
    for config_status in commands_to_ep:
        config_sent = ssh_connect.send_command(config_status)    #Sending command to accessed endpoints
        print(config_sent)


end_time= datetime.now()                    #end of main script

total_time = end_time - start_time
print(total_time)           #Time taken for all