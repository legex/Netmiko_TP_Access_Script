from netmiko import*
from datetime import*
import csv
import os
import sys

class TelepresemceAccess:

    def __init__(self,**kwargs):
        self.kwargs=kwargs
    #Defining function

    def single_tp_access(self,hostname,target_user,target_pass,command_to_ep):
        '''
        Function to defile base information and initiate connection with units provided
        '''
        vc_endpoint = {
            'device_type':'cisco_tp',
            'ip':'',
            'username':'',
            'password':'',
            'port':'22',
            'timeout':3.5,
            }                                                                       #dictionary to store values

        vc_endpoint['ip']= str(hostname)                                            #assigning new values to place holder
        vc_endpoint['username']=target_user
        vc_endpoint['password']= str(target_pass)
        
        
        parent_dir='C:/path/to/Documents/'
        create_dir= 'test'+str(date.today())
        dir_path=os.path.join(parent_dir,create_dir)
        os.mkdir(dir_path)
        
        ssh_connect=ConnectHandler(**vc_endpoint)                                   #connection initiation
        try:
            print('Connection established with:{}'.format(vc_endpoint['ip']))
            destination_path = os.path.join(dir_path,vc_endpoint['ip'])
            os.mkdir(destination_path)
            destination_file = os.path.join(destination_path,vc_endpoint['ip']+'.txt')
            access_file=open(destination_file,'a')
            access_file.write("Accessing Video Unit: {}".format(vc_endpoint['ip'])+'\n')
            access_file.write(ssh_connect.find_prompt())
            access_file.write('\n==================================================\n')
        
            print(ssh_connect.find_prompt())                                         
            config_sent = ssh_connect.send_command(command_to_ep)                       #send command to device
            access_file.write(config_sent)
            access_file.write('\n==================================================\n')
            print(config_sent)
            access_file.close()
        except (NetMikoAuthenticationException):
            print('Authentication Failed')
        except (NetMikoTimeoutException):
            print('Connection failed')
        
    
    
    def multiple_access(self,vc_input_file,command_file):
        vc_lst=[]
        commands_to_ep=[]
        with open(command_file,'r') as ep_commands: #parsing text command file and appending them to list
            for lines in ep_commands:
                commands_to_ep.append(lines)
        
        with open(vc_input_file,'r') as vcfile:
            for vcunits in csv.DictReader(vcfile): #Reading input data using and converting to dictionary
                vcunits.update({'device_type':'cisco_tp'})          #Adding arguements for dictionary
                vcunits.update({'username': target_user})
                vcunits.update({'password':target_pass})
                vcunits.update({'port':'22'})
                vcunits.update({'timeout': 8})
                vcunits.update({'global_delay_factor':1})
                vcunits.pop('System Name')                          #Poping out extra attribute
                vc_lst.append(vcunits)                                       #Adding dictionary to empty list

        parent_dir='C:/path/to/Documents/'
        create_dir= 'test'+str(date.today())
        dir_path=os.path.join(parent_dir,create_dir)
        os.mkdir(dir_path)
    
        for video_units in vc_lst:                                                  #loop to initiate connections for all items in list
            try:

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
            except (NetMikoTimeoutException):
                print('Connection Timeout')
            except (NetMikoAuthenticationException):
                print('Authentication Failed')
            finally:
                continue


tp_access=TelepresemceAccess()

user_action=input('What do we do today?\n Your options are: \n 1-Access one TP \n 2-Access Multiple TP \n Your Input:')

if int(user_action) == 1 or user_action=='single tp access':
    print('Accessing 1 TP, Okay!\n Provide below info:')
    hostname = input('Target IP:')              
    target_user = input('Enter username:')
    target_pass= input('Enter password:')
    command_to_ep=input('send command:')
    tp_access.single_tp_access(hostname,target_user,target_pass,command_to_ep)

elif int(user_action) == 2 or user_action=='multiple tp access':
    print('Accessing multiple tps now, okay')
    target_user=input('Provide username:')
    target_pass=input('Provide Password:')
    vc_input_file="Test_file.csv" 
    command_file="commands.txt"
    
    start_time= datetime.now()
    
    tp_access.multiple_access(vc_input_file,command_file)
    
    end_time= datetime.now()
    
    total_time = end_time - start_time
    print(total_time)           #Time taken for all
else:
    print('Invalid input \n Closing program')
    sys.exit()
