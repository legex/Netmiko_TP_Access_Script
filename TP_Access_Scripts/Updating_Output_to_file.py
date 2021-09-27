from netmiko import*
from datetime import*
import csv
import os



target_user=input('Provide username:')
target_pass=input('Provide Password:')

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
        vcunits.update({'device_type':'cisco_tp'})          #Adding arguements for dictionary
        vcunits.update({'username': target_user})
        vcunits.update({'password':target_pass})
        vcunits.update({'port':'22'})
        vcunits.update({'global_delay_factor':1})
        vcunits.pop('System Name')                          #Poping out extra attribute
        vc_lst.append(vcunits)                                       #Adding dictionary to empty list

parent_dir='C:/Users/RCGR8654/Documents/'
create_dir= 'test'+str(date.today())
dir_path=os.path.join(parent_dir,create_dir)
os.mkdir(dir_path)

start_time= datetime.now()                                                   #Starting of main script


for video_units in vc_lst:                                                  #loop to initiate connections for all items in list
    ssh_connect=ConnectHandler(**video_units)
    print("Accessing Video Unit: {}".format(video_units['ip']))
    
    '''Creating new dir to save the o/p as per folders
    and creating .txt files per endpoint with in folders
    '''
    destination_path = os.path.join(dir_path,video_units['ip'])
    os.mkdir(destination_path)
    destination_file = os.path.join(destination_path,video_units['ip']+'.txt')
    access_file=open(destination_file,'a')
    access_file.write("Accessing Video Unit: {}".format(video_units['ip'])+'\n')
    access_file.write(ssh_connect.find_prompt())
    access_file.write('\n==================================================\n')
    
    
    print(ssh_connect.find_prompt())                                         #Connection output
    for config_status in commands_to_ep:
        config_sent = ssh_connect.send_command(config_status)                #Sending command to accessed endpoints
        access_file.write(config_sent)
        access_file.write('\n==================================================\n')
    access_file.close()


end_time= datetime.now()                    #end of main script

total_time = end_time - start_time
print(total_time)           #Time taken for all
