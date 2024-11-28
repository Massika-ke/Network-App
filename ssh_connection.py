import paramiko
import os.path
import time
import sys
import re

#check username/password file
#prompt for user input-file
user_file = input("\n# Enter the user file path :")

#verify the validity of file
if os.path.isfile(user_file) == True:
    print("\n* File is valid :)\n")

else:
    print("\n* File {} does not exist :(please check and try again.\n".format(user_file))
    sys.exit()
    
#check commands file
#Prompt for user input
cmd_file = input("\n# Enter commands file path :")

#verify validity of commands file
if os.path.isfile(cmd_file) == True:
    print("\n* command file is valid :) \n")

else:
    print("\n* File does not exist :( please check and try again.\n".format(cmd_file))
    sys.exit() 
    
#Open SSHv2 connection to the device
def ssh_connection(ip):

    global user_file
    global cmd_file  

    #create SSH connection
    try:
        #define SSH parameters
        #open file for reading
        selected_user_file = open(user_file, 'r')
        #start from beginning
        selected_user_file.seek(0)
        #reading the username from file
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        #starting from the beginning of file
        selected_user_file.seek(0)
        #reading password
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        #logging into the device/SSH Client
        session = paramiko.SSHClient()
        
        #Auto accept unknown host keys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #connect to device using username and password
        session.connect(ip.rstrip("\n"), username = username, password = password)

        #start an interactictive shell session on th router
        connection = session.invoke_shell()

        #setting terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        #entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        #open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')

        #starting from the beginning of the file
        selected_cmd_file.seek(0)

        #writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        #closing the user file
        selected_user_file.close()
        #close the cmd file
        selected_cmd_file.close()

        #check command output for syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))

        else:
            print("\nDONE for device {} :)\n".format(ip))

        #test for reading command output
        # print(str(router_output)+ "\n")

        #close connection
        session.close()

    except paramiko.AuthenticationException:
        print("*Invalid Username or password :")
        print("* Closing program...")

